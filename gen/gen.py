import json, re, unicodedata, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data_geo import *
from data_nature import *
from data_food import *
from data_culture import *
from data_misc import *

STOP = set('o a os as um uma de do da dos das e'.split())

def key(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
    out = []
    for w in s.split():
        if not w or w in STOP: continue
        if len(w) > 3 and w.endswith('s'): w = w[:-1]
        out.append(w)
    return ''.join(out)

def letters_ok(word, letters):
    w = key(word)
    if len(w) < 3: return False
    pool = list(key(letters))
    for ch in w:
        if ch in pool: pool.remove(ch)
        else: return False
    return True

def parse(text, letters=None):
    seen, out = set(), []
    for raw in text.replace('\n', ' ').split(';'):
        raw = raw.strip()
        if not raw or raw.endswith('?'): continue
        names = [n.strip() for n in raw.split('/') if n.strip()]
        k0 = key(names[0])
        if not k0 or k0 in seen: continue
        if letters and not letters_ok(names[0], letters): continue
        al = []
        for n in names:
            k = key(n)
            if k and k not in seen:
                seen.add(k); al.append(n)
        if al: out.append(al)
    return out

PROMPTS = []
def P(pid, q, g, text, letters=None):
    entries = parse(text, letters)
    d = {'id': pid, 'q': q, 'g': g, 'a': ';'.join('/'.join(e) for e in entries)}
    if letters: d['l'] = letters
    PROMPTS.append(d)
    return entries

def derive(pid, base_entries, label, g, letters_list, minimum=12):
    for L in letters_list:
        sub = [e for e in base_entries if key(e[0]).startswith(L.lower())]
        if len(sub) >= minimum:
            PROMPTS.append({'id': f'{pid}-{L.lower()}', 'q': f'{label} que começa com a letra {L}', 'g': g,
                            'a': ';'.join('/'.join(e) for e in sub)})

# ---- Geography
paises_txt = ';'.join([PAIS_TOP, SUL, NORTE, EUROPA, AFRICA, ASIA, OCEANIA])
paises = P('pais', 'Um país do mundo', 'pais', paises_txt)
P('europa', 'Um país da Europa', 'pais', EUROPA)
P('africa', 'Um país da África', 'pais', AFRICA)
P('asia', 'Um país da Ásia', 'pais', ASIA)
P('americas', 'Um país das Américas', 'pais', ';'.join([SUL.replace('Brasil;', ''), NORTE]))
P('oceania', 'Um país ou território da Oceania', 'pais', OCEANIA)
P('caribe', 'Um país da América Central ou do Caribe', 'pais', NORTE.split(';', 3)[3])
derive('pais', paises, 'Um país', 'pais-l', list('ABCEGILMNPST'))
caps = P('capital', 'A capital de um país', 'capital', CAPITAIS)
derive('capital', caps, 'Uma capital de país', 'capital-l', list('BMPS'))
P('cap', 'Uma capital de estado brasileiro', 'br-geo', CAP_BR)
P('uf', 'Um estado brasileiro (ou o DF)', 'br-geo', UF)
P('cidade-rj', 'Uma cidade do estado do Rio de Janeiro', 'rio', CIDADE_RJ)
P('bairro-rio', 'Um bairro da cidade do Rio de Janeiro', 'rio', BAIRRO_RIO)
P('ponto-rio', 'Um ponto turístico do Rio de Janeiro', 'rio', PONTO_RIO)
P('rio-br', 'Um rio brasileiro', 'br-geo', RIO_BR)
P('eua', 'Um estado dos Estados Unidos', 'eua', ESTADO_EUA)
P('mar', 'Um oceano, mar ou golfo', 'mar', OCEANO)
P('montanha', 'Uma montanha, vulcão, serra ou cordilheira', 'montanha', MONTANHA)

# ---- Nature
frutas = P('fruta', 'Uma fruta', 'fruta', FRUTA)
derive('fruta', frutas, 'Uma fruta', 'fruta-l', list('ABCGJMP'))
P('legume', 'Um legume, verdura ou hortaliça', 'legume', LEGUME)
mams = P('mamifero', 'Um mamífero', 'mamifero', MAMIFERO)
derive('mamifero', mams, 'Um mamífero', 'mamifero-l', list('BCGLMPT'))
P('fauna', 'Um animal da fauna brasileira', 'fauna', FAUNA_BR)
aves = P('ave', 'Uma ave', 'ave', AVE)
derive('ave', aves, 'Uma ave', 'ave-l', list('ACGPST'))
P('peixe', 'Um peixe', 'peixe', PEIXE)
P('inseto', 'Um inseto', 'inseto', INSETO)
P('dino', 'Um dinossauro ou réptil pré-histórico', 'dino', DINO)
P('cao', 'Uma raça de cachorro', 'cao', RACA_CAO)
P('gato', 'Uma raça de gato', 'gato', RACA_GATO)
P('marinho', 'Um animal marinho', 'marinho', ANIMAL_MAR)
P('flor', 'Uma flor', 'flor', FLOR)
P('arvore', 'Uma árvore', 'arvore', ARVORE)
P('tempero', 'Um tempero, erva ou especiaria', 'tempero', TEMPERO)

# ---- Food
pratos = P('prato', 'Uma comida típica brasileira', 'comida', PRATO_BR)
P('doce', 'Um doce brasileiro', 'doce', DOCE_BR)
P('salgado', 'Um salgado de lanchonete ou de festa', 'salgado', SALGADO)
P('pizza', 'Um sabor de pizza', 'pizza', PIZZA)
P('sorvete', 'Um sabor de sorvete', 'sorvete', SORVETE)
P('queijo', 'Um tipo de queijo', 'queijo', QUEIJO)
P('bebida', 'Uma bebida alcoólica', 'bebida', BEBIDA_ALC)
P('drink', 'Um drinque ou coquetel', 'drink', DRINK)
P('italiana', 'Um prato ou doce italiano', 'italiana', PRATO_ITA)
P('japonesa', 'Uma comida japonesa', 'japonesa', JAPONESA)
P('junina', 'Uma comida ou bebida de festa junina', 'junina', FESTA_JUNINA)
P('marca-doce', 'Uma marca de chocolate, bala ou biscoito', 'marca-doce', MARCA_DOCE)
P('fastfood', 'Uma rede de fast food ou restaurante', 'fastfood', FASTFOOD)

# ---- Brazilian culture
P('clube', 'Um clube campeão brasileiro da Série A', 'clube', CLUBE_CAMPEAO)
P('clube-br', 'Um clube de futebol brasileiro', 'clube', CLUBE_BR)
P('novela', 'Uma novela da Globo', 'novela', NOVELA)
P('monica', 'Um personagem da Turma da Mônica', 'monica', MONICA)
P('folk', 'Uma figura ou lenda do folclore brasileiro', 'folk', FOLCLORE)
P('samba', 'Uma escola de samba do Rio de Janeiro', 'samba', SAMBA)
P('presidente', 'Um presidente do Brasil', 'presidente', PRESIDENTE)
P('penta', 'Um jogador campeão do mundo pela Seleção Brasileira', 'penta', TETRA_PENTA)
P('cantor', 'Um cantor ou cantora brasileiro(a)', 'cantor', CANTOR_BR)
P('banda', 'Uma banda, grupo ou dupla brasileira', 'banda', BANDA_BR)
P('globo', 'Um programa da TV Globo (sem contar novelas)', 'globo', PROGRAMA_GLOBO)
P('chaves', 'Um personagem de Chaves ou Chapolin', 'chaves', CHAVES)
P('sitio', 'Um personagem do Sítio do Picapau Amarelo', 'sitio', SITIO)

# ---- Pop culture & games
pk = P('pokemon1', 'Um Pokémon da 1ª geração (Kanto)', 'pokemon', POKEMON1)
derive('pokemon1', pk, 'Um Pokémon da 1ª geração', 'pokemon-l', list('CGKMPS'), 10)
P('pokemon', 'Um Pokémon de qualquer geração', 'pokemon', POKEMON1 + ';' + POKEMON_MAIS)
P('lol', 'Um campeão de League of Legends', 'lol', LOL)
P('valorant', 'Um agente de Valorant', 'valorant', VALORANT)
P('minecraft', 'Um mob ou criatura do Minecraft', 'minecraft', MINECRAFT)
P('mario', 'Um personagem do universo Mario', 'mario', MARIO)
P('harry', 'Um personagem de Harry Potter', 'harry', HARRY)
P('pixar', 'Um filme da Pixar', 'pixar', PIXAR)
P('marvel', 'Um personagem da Marvel', 'marvel', MARVEL)
P('dc', 'Um personagem da DC', 'dc', DC)
P('dbz', 'Um personagem de Dragon Ball', 'dbz', DRAGONBALL)
P('naruto', 'Um personagem de Naruto', 'naruto', NARUTO)

# ---- Science, everyday, misc
P('instr', 'Um instrumento musical', 'instr', INSTR)
P('cor', 'Uma cor', 'cor', COR)
P('astro', 'Um planeta, planeta anão ou lua do Sistema Solar', 'astro', ASTRO)
P('olimp', 'Um esporte ou prova que já foi disputado em Olimpíadas de verão', 'olimp', OLIMP)
P('esporte', 'Um esporte', 'esporte', ESPORTE)
P('luta', 'Uma arte marcial ou luta', 'luta', ARTE_MARCIAL)
P('xadrez', 'Uma abertura ou defesa de xadrez', 'xadrez', XADREZ)
P('jogo', 'Um jogo de tabuleiro ou de cartas', 'jogo', JOGO_MESA)
P('tech', 'Uma marca de eletrônicos ou tecnologia', 'tech', MARCA_TECH)
P('app', 'Um aplicativo, site ou rede social', 'app', APP)
P('roupa-marca', 'Uma marca de roupa ou calçado', 'roupa-marca', ROUPA_MARCA)
P('banco', 'Um banco brasileiro (atual ou antigo)', 'banco', BANCO)
P('loja', 'Uma loja, rede ou supermercado no Brasil', 'loja', LOJA)
P('profissao', 'Uma profissão', 'profissao', PROFISSAO)
P('roupa', 'Uma peça de roupa ou calçado', 'roupa', ROUPA)
P('casa', 'Um cômodo, móvel ou parte de uma casa', 'casa', CASA)
P('eletro', 'Um eletrodoméstico ou aparelho eletrônico', 'eletro', ELETRO)
P('ferramenta', 'Uma ferramenta', 'ferramenta', FERRAMENTA)
P('transporte', 'Um meio de transporte', 'transporte', TRANSPORTE)
P('danca', 'Uma dança ou estilo de dança', 'danca', DANCA)
P('grega', 'Um deus, herói ou criatura da mitologia grega', 'mito', MITO_GREGA)
P('nordica', 'Um deus ou criatura da mitologia nórdica', 'mito', MITO_NORDICA)
P('egito', 'Um deus ou deusa do Egito antigo', 'mito', MITO_EGITO)
P('moeda', 'Uma moeda (atual, antiga ou cripto)', 'moeda', MOEDA)
P('feriado', 'Um feriado ou data comemorativa', 'feriado', FERIADO)
P('constelacao', 'Uma constelação', 'constelacao', CONSTELACAO)
P('osso', 'Um osso do corpo humano', 'corpo', OSSO)
P('orgao', 'Um órgão ou parte interna do corpo humano', 'corpo', ORGAO)
P('forma', 'Uma forma geométrica', 'forma', FORMA)
P('unidade', 'Uma unidade de medida', 'unidade', UNIDADE)
el = P('elem', 'Um elemento da tabela periódica', 'elem', ELEM)
derive('elem', el, 'Um elemento químico', 'elem-l', list('CP'), 10)
P('idioma', 'Um idioma além do português', 'idioma', IDIOMA)
P('genero', 'Um gênero ou ritmo musical', 'genero', GENERO)
for w, txt in LETRAS:
    P('letras-' + w, f'Uma palavra de 3+ letras usando só as letras de {w.upper()}', 'letras', txt, letters=w)

# ---- Obscurity ratings (1 = obvious ... 7 = extremely obscure), produced once by the rating job.
# ratings.json: {prompt_id: [rating per answer, in list order]}. Letter variants reuse their base prompt's ratings.
RATINGS = {}
rp = os.path.join(HERE, 'ratings.json')
if os.path.exists(rp):
    RATINGS = {k: [int(c) for c in v] if isinstance(v, str) else v for k, v in json.load(open(rp, encoding='utf-8')).items()}

def finish(p):
    entries = p['a'].split(';')
    if p['g'].endswith('-l'):
        base_id = p['id'].rsplit('-', 1)[0]
        p['s'] = p['id'].rsplit('-', 1)[1].upper()
        base = next(b for b in PROMPTS if b['id'] == base_id)
        base_names = [e.split('/')[0] for e in base['a'].split(';')]
        br = RATINGS.get(base_id, [])
        by_name = {n: (br[i] if i < len(br) else 4) for i, n in enumerate(base_names)}
        r = [by_name.get(e.split('/')[0], 4) for e in entries]
    else:
        rr = RATINGS.get(p['id'], [])
        r = [rr[i] if i < len(rr) else 4 for i in range(len(entries))]
    # "Um em um milhão": the 2 most obscure answers of each prompt (only if they are at least "obscura")
    order = sorted(range(len(entries)), key=lambda i: (-r[i], -i))
    top = [i for i in order[:2] if r[i] >= 6]
    r = [6 if x == 7 else x for x in r]
    for i in top:
        r[i] = 7
    p['a'] = ';'.join(f'{e}#{x}' for e, x in zip(entries, r))

for p in PROMPTS:
    if not p['g'].endswith('-l'):
        p['_raw'] = p['a']
for p in PROMPTS:
    if p['g'].endswith('-l'):
        finish(p)
for p in PROMPTS:
    if not p['g'].endswith('-l'):
        finish(p)
for p in PROMPTS:
    p.pop('_raw', None)

ids = [p['id'] for p in PROMPTS]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
json.dump(PROMPTS, open(os.path.join(HERE, '..', 'site', 'prompts.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
tot = sum(len(p['a'].split(';')) for p in PROMPTS)
print(len(PROMPTS), 'prompts', tot, 'answers')
for p in PROMPTS:
    n = len(p['a'].split(';'))
    if n < 15: print('  small:', p['id'], n)
