-- Leaderboard rows carry an opaque ref (not the player id); details are only shown
-- to players who already finished that day's dive, so nobody can copy answers.
drop function if exists public.leaderboard(date);
create function public.leaderboard(p_day date)
returns table (ref text, nickname text, score int, is_me boolean)
language sql stable security definer set search_path = public as $$
  select md5(d.player_id::text || d.day::text), coalesce(p.nickname, 'Mergulhador'), d.score, d.player_id = auth.uid()
  from public.dives d left join public.players p on p.id = d.player_id
  where d.day = p_day and d.done
  order by d.score desc, d.updated_at asc
  limit 20;
$$;

create or replace function public.dive_details(p_day date, p_ref text)
returns table (nickname text, prompt_ids text[], answers text[], tiers int[], points int[], score int)
language plpgsql stable security definer set search_path = public as $$
begin
  if not exists (select 1 from public.dives where player_id = auth.uid() and day = p_day and done) then
    raise exception 'finish your dive first' using errcode = 'insufficient_privilege';
  end if;
  return query
    select coalesce(p.nickname, 'Mergulhador'), d.prompt_ids, d.answers, d.tiers, d.points, d.score
    from public.dives d left join public.players p on p.id = d.player_id
    where d.day = p_day and d.done and md5(d.player_id::text || d.day::text) = p_ref;
end $$;

revoke all on function public.leaderboard(date), public.dive_details(date, text) from public, anon;
grant execute on function public.leaderboard(date), public.dive_details(date, text) to authenticated;
