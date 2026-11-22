-- Rarity v2: obscurity ratings (1-7) and the "Um em um milhão" tier

create extension if not exists pg_net;

alter table public.extras add column if not exists rating int check (rating between 1 and 7);
alter table public.dives drop constraint if exists dives_score_check;
alter table public.dives add constraint dives_score_check check (score between 0 and 1050);

-- Batch job that rates the built-in answer lists (see supabase/functions/rate)
create table if not exists public.ratings (
  prompt_id  text not null,
  start      int  not null,
  ratings    int[],
  error      text,
  created_at timestamptz not null default now(),
  primary key (prompt_id, start)
);
create table if not exists public.rating_jobs (token text primary key, created_at timestamptz not null default now());
alter table public.ratings enable row level security;
alter table public.rating_jobs enable row level security;

drop function if exists public.get_extras(text[]);
create function public.get_extras(p_ids text[])
returns table (prompt_id text, answer_key text, name text, rating int)
language sql stable security definer set search_path = public as $$
  select e.prompt_id, e.answer_key, e.name, e.rating
  from public.extras e
  where e.prompt_id = any (p_ids) and e.status in ('auto_ok','approved');
$$;
revoke all on function public.get_extras(text[]) from public, anon;
grant execute on function public.get_extras(text[]) to authenticated;
