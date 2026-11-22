-- Abissal: database schema
-- Players sign in anonymously (Supabase anonymous auth), so every visitor gets a stable user id.

-- ---------------------------------------------------------------- tables

-- Nickname shown on the leaderboard
create table public.players (
  id          uuid primary key references auth.users(id) on delete cascade,
  nickname    text not null check (char_length(btrim(nickname)) between 2 and 20),
  created_at  timestamptz not null default now()
);

-- One row per player per prompt: the answer they gave the last time that prompt came up.
-- Rarity = how many OTHER players share your answer_key for that prompt.
create table public.answers (
  prompt_id    text not null check (char_length(prompt_id) between 1 and 40),
  player_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  answer_key   text not null check (char_length(answer_key) between 1 and 80),
  answer_name  text not null check (char_length(answer_name) between 1 and 80),
  day          date not null,
  updated_at   timestamptz not null default now(),
  primary key (prompt_id, player_id)
);
create index answers_prompt_key on public.answers (prompt_id, answer_key);

-- One row per player per day: progress and score of the daily dive
create table public.dives (
  player_id   uuid not null default auth.uid() references auth.users(id) on delete cascade,
  day         date not null,
  prompt_ids  text[] not null check (cardinality(prompt_ids) <= 7),
  answers     text[] not null default '{}' check (cardinality(answers) <= 7),
  tiers       int[]  not null default '{}' check (cardinality(tiers) <= 7),
  points      int[]  not null default '{}' check (cardinality(points) <= 7),
  score       int    not null default 0 check (score between 0 and 700),
  done        boolean not null default false,
  updated_at  timestamptz not null default now(),
  primary key (player_id, day)
);
create index dives_day_score on public.dives (day, score desc);

-- Answers that were not on the built-in lists. Filled only by the judge function.
--   auto_ok / auto_no : Claude's decision, waiting for your review
--   approved / rejected : your final decision (overrides Claude)
create table public.extras (
  prompt_id     text not null,
  answer_key    text not null,
  name          text not null,
  status        text not null check (status in ('auto_ok','auto_no','approved','rejected')),
  raw_answer    text,
  first_player  uuid references auth.users(id) on delete set null,
  created_at    timestamptz not null default now(),
  reviewed_at   timestamptz,
  primary key (prompt_id, answer_key)
);
create index extras_status on public.extras (status, created_at desc);

-- Each call to Claude, for the per-player daily limit
create table public.judge_log (
  id          bigint generated always as identity primary key,
  player_id   uuid not null,
  created_at  timestamptz not null default now()
);
create index judge_log_player on public.judge_log (player_id, created_at desc);

-- Who can use the review page
create table public.admins (
  user_id uuid primary key references auth.users(id) on delete cascade
);

-- ---------------------------------------------------------------- row level security

alter table public.players   enable row level security;
alter table public.answers   enable row level security;
alter table public.dives     enable row level security;
alter table public.extras    enable row level security;
alter table public.judge_log enable row level security;
alter table public.admins    enable row level security;

create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.admins where user_id = auth.uid());
$$;

-- Players read and write only their own rows. Other people's data is reached only through the functions below.
create policy players_own on public.players for all to authenticated
  using (id = auth.uid()) with check (id = auth.uid());
create policy answers_own on public.answers for all to authenticated
  using (player_id = auth.uid()) with check (player_id = auth.uid());
create policy dives_own on public.dives for all to authenticated
  using (player_id = auth.uid()) with check (player_id = auth.uid());

-- Extras: only admins read and review. The judge function writes with the service role, which bypasses RLS.
create policy extras_admin_read on public.extras for select to authenticated using (public.is_admin());
create policy extras_admin_update on public.extras for update to authenticated
  using (public.is_admin()) with check (public.is_admin());
-- judge_log and admins have no policies: invisible to players.

-- ---------------------------------------------------------------- functions the site calls

-- How many other players gave each answer, for some prompts
create or replace function public.get_counts(p_ids text[])
returns table (prompt_id text, answer_key text, n int)
language sql stable security definer set search_path = public as $$
  select a.prompt_id, a.answer_key, count(*)::int
  from public.answers a
  where a.prompt_id = any (p_ids)
    and a.player_id is distinct from auth.uid()
  group by a.prompt_id, a.answer_key;
$$;

-- Accepted answers that are not on the built-in lists
create or replace function public.get_extras(p_ids text[])
returns table (prompt_id text, answer_key text, name text)
language sql stable security definer set search_path = public as $$
  select e.prompt_id, e.answer_key, e.name
  from public.extras e
  where e.prompt_id = any (p_ids) and e.status in ('auto_ok','approved');
$$;

-- Today's leaderboard
create or replace function public.leaderboard(p_day date)
returns table (nickname text, score int, is_me boolean)
language sql stable security definer set search_path = public as $$
  select coalesce(p.nickname, 'Mergulhador'), d.score, d.player_id = auth.uid()
  from public.dives d left join public.players p on p.id = d.player_id
  where d.day = p_day and d.done
  order by d.score desc, d.updated_at asc
  limit 20;
$$;

-- Number of distinct players who have ever answered
create or replace function public.player_count()
returns int language sql stable security definer set search_path = public as $$
  select count(distinct player_id)::int from public.answers;
$$;

revoke all on function public.get_counts(text[]), public.get_extras(text[]), public.leaderboard(date),
  public.player_count(), public.is_admin() from public;
grant execute on function public.get_counts(text[]), public.get_extras(text[]), public.leaderboard(date),
  public.player_count(), public.is_admin() to anon, authenticated;

-- Every player is signed in (anonymously), so the anon role needs none of these
revoke execute on function public.get_counts(text[]), public.get_extras(text[]), public.leaderboard(date),
  public.player_count(), public.is_admin() from anon;
