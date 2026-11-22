-- Nicknames are written only by the "nickname" Edge Function (service role), never directly by players.
drop policy if exists players_own on public.players;
create policy players_read_own on public.players for select to authenticated using (id = auth.uid());

alter table public.judge_log add column if not exists kind text not null default 'judge';

-- Last line of defense: unambiguous slurs/obscenities, matched after normalizing accents, leetspeak,
-- separators and repeated letters. Gray areas are left to the moderation model in the function.
create or replace function public.nick_normalize(t text) returns text
language sql immutable as $$
  select regexp_replace(
           translate(lower(t), 'áàâãäéèêëíìîïóòôõöúùûüçñ013457@$!|', 'aaaaaeeeeiiiiooooouuuucnoieastasii'),
         '[^a-z]', '', 'g');
$$;

create or replace function public.nick_blocked(t text) returns boolean
language sql immutable as $$
  select exists (
    select 1 from unnest(array[
      'nigg','niga','nigger','negrosujo','macacopreto','odeio','viado','traveco','sapatao','bichona',
      'filhodaputa','putaria','putinha','caralho','porra','buceta','boceta','cuzao','cuzinho','arrombad',
      'foder','fuder','fodase','fodido','piroca','xoxota','xereca','punheta','vagabund','retardad','escrot',
      'merda','bosta','estupr','pedofil','hitler','nazi','suastica','kukluxklan',
      'fuck','bitch','cunt','faggot','retard','whore','slut','penis','vagina','porn'
    ]) w
    where position(w in public.nick_normalize(t)) > 0
       or position(w in regexp_replace(public.nick_normalize(t), '(.)\1+', '\1', 'g')) > 0
  );
$$;

create or replace function public.players_nick_guard() returns trigger
language plpgsql as $$
begin
  if public.nick_blocked(new.nickname) then
    raise exception 'nickname not allowed' using errcode = 'check_violation';
  end if;
  return new;
end $$;

drop trigger if exists players_nick_guard on public.players;
create trigger players_nick_guard before insert or update of nickname on public.players
for each row execute function public.players_nick_guard();

update public.players set nickname = 'Mergulhador ' || upper(substr(id::text, 1, 4))
where public.nick_blocked(nickname);
