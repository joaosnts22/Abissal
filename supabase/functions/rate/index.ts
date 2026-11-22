// One-off batch job: rates how obvious/obscure every built-in answer is (1 = obvious … 7 = extremely obscure).
// Started from SQL with a token stored in public.rating_jobs; each run handles one chunk and then calls itself
// for the next one, pacing requests to stay inside the Gemini free tier.
import { createClient } from "npm:@supabase/supabase-js@2";

const GEMINI_API_KEY = Deno.env.get("GEMINI_API_KEY") ?? "";
const GEMINI_MODEL = Deno.env.get("GEMINI_MODEL") ?? "gemini-3.5-flash-lite";
const PROMPTS_URL = Deno.env.get("PROMPTS_URL") ?? "https://joaosnts22.github.io/Abissal/prompts.json";
const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const CHUNK = 100;
const PAUSE_MS = 4500;

type Prompt = { id: string; q: string; g: string; a: string; l?: string };
type Chunk = { id: string; q: string; start: number; names: string[] };
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

let chunks: Chunk[] | null = null;
async function loadChunks(): Promise<Chunk[]> {
  if (chunks) return chunks;
  const list = (await (await fetch(PROMPTS_URL)).json()) as Prompt[];
  const out: Chunk[] = [];
  for (const p of list) {
    if (p.g.endsWith("-l")) continue; // letter variants reuse their base list's ratings
    const names = p.a.split(";").map((x) => x.split("#")[0].split("/")[0]);
    for (let s = 0; s < names.length; s += CHUNK) out.push({ id: p.id, q: p.q, start: s, names: names.slice(s, s + CHUNK) });
  }
  return (chunks = out);
}

async function rateChunk(c: Chunk): Promise<number[]> {
  const prompt =
    `Você vai estimar o quão óbvia ou obscura é cada resposta para uma pergunta de um jogo de trivia brasileiro, ` +
    `em que jogadores brasileiros comuns têm 25 segundos para dar qualquer resposta correta.\n` +
    `Pergunta: "${c.q}"\n\nEscala:\n` +
    `1 = óbvia, das primeiras que vêm à cabeça de quase todo mundo\n` +
    `2 = comum, muita gente daria\n` +
    `3 = conhecida, mas poucos lembrariam na hora\n` +
    `4 = rara, só quem gosta do assunto lembraria\n` +
    `5 = muito rara\n` +
    `6 = obscura, quase nenhum brasileiro daria\n` +
    `7 = extremamente obscura, praticamente só especialistas conhecem\n\n` +
    `Seja exigente e realista: coisas do dia a dia dos brasileiros ficam entre 1 e 3, mesmo que não sejam as primeiras da lista. ` +
    `Use 6 e 7 só para o que um brasileiro médio provavelmente nem conhece.\n\nRespostas:\n` +
    c.names.map((n, i) => `${i}. ${n}`).join("\n") +
    `\n\nResponda só com JSON: {"r": [nota da resposta 0, nota da resposta 1, ...]} com exatamente ${c.names.length} números inteiros de 1 a 7.`;
  const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent`, {
    method: "POST",
    headers: { "x-goog-api-key": GEMINI_API_KEY, "content-type": "application/json" },
    body: JSON.stringify({
      contents: [{ role: "user", parts: [{ text: prompt }] }],
      generationConfig: { temperature: 0, maxOutputTokens: 4096, responseMimeType: "application/json" },
    }),
  });
  if (!res.ok) throw Object.assign(new Error(`Gemini ${res.status}: ${(await res.text()).slice(0, 300)}`), { status: res.status });
  const data = await res.json();
  const text = (data?.candidates?.[0]?.content?.parts ?? []).filter((p: { text?: string; thought?: boolean }) => p.text && !p.thought)
    .map((p: { text: string }) => p.text).join("");
  const r = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1)).r;
  if (!Array.isArray(r) || r.length !== c.names.length) throw new Error(`bad length ${r?.length} vs ${c.names.length}`);
  return r.map((x: unknown) => Math.min(7, Math.max(1, Math.round(Number(x)) || 3)));
}

async function kick(token: string, i: number, tries: number) {
  await fetch(`${SUPABASE_URL}/functions/v1/rate`, {
    method: "POST",
    headers: { "content-type": "application/json", Authorization: `Bearer ${SERVICE_KEY}`, apikey: SERVICE_KEY },
    body: JSON.stringify({ token, i, tries }),
  }).catch((e) => console.error("kick failed", e));
}

Deno.serve(async (req) => {
  const { token, i = 0, tries = 0 } = await req.json().catch(() => ({}));
  const db = createClient(SUPABASE_URL, SERVICE_KEY, { auth: { persistSession: false } });
  const { data: job } = await db.from("rating_jobs").select("token").eq("token", String(token ?? "")).maybeSingle();
  if (!job) return new Response("forbidden", { status: 403 });

  const work = (async () => {
    const all = await loadChunks();
    if (i >= all.length) { console.log("rating job finished", all.length); return; }
    const c = all[i];
    const { data: done } = await db.from("ratings").select("ratings").eq("prompt_id", c.id).eq("start", c.start).maybeSingle();
    if (!done?.ratings) {
      try {
        const r = await rateChunk(c);
        await db.from("ratings").upsert({ prompt_id: c.id, start: c.start, ratings: r, error: null });
      } catch (e) {
        const msg = String((e as Error).message);
        if (tries < 4) { await sleep((e as { status?: number }).status === 429 ? 30000 : 5000); return kick(token, i, tries + 1); }
        await db.from("ratings").upsert({ prompt_id: c.id, start: c.start, ratings: null, error: msg });
      }
      await sleep(PAUSE_MS);
    }
    await kick(token, i + 1, 0);
  })();
  // @ts-ignore EdgeRuntime is provided by Supabase
  EdgeRuntime.waitUntil(work);
  return new Response(JSON.stringify({ started: i }), { headers: { "content-type": "application/json" } });
});
