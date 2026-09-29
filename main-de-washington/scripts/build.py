# Assemble les pages : gabarit + géométrie de la carte + base d'incidents + traductions
#   -> index.html (français) et index.<langue>.html pour chaque traduction disponible.
# Usage : python3 scripts/build.py
# Traductions : donnees/traductions/<langue>.json = {"ui": {...}, "pays": {nom français: nom traduit},
#   "faits": {clé: [titre, lieu, note]}}. La clé d'un fait est sha1("date|titre français")[:10] (voir cle()).
# Un fait non traduit s'affiche en français.
import os, json, hashlib, html

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
lire = lambda *p: open(os.path.join(R, *p), encoding='utf-8').read()

# ordre d'affichage du sélecteur de langue
LANGUES = ['fr', 'en', 'es', 'pt', 'ar', 'zh', 'hi', 'bn', 'ru', 'id']
RTL = {'ar'}
# polices complémentaires pour les écritures que Syne et JetBrains Mono ne couvrent pas
POLICES = {
    'zh': ('Noto+Sans+SC:wght@400;700;900', '"Noto Sans SC"', '"Noto Sans SC"'),
    'hi': ('Noto+Sans+Devanagari:wght@400;700;800', '"Noto Sans Devanagari"', '"Noto Sans Devanagari"'),
    'bn': ('Noto+Sans+Bengali:wght@400;700;800', '"Noto Sans Bengali"', '"Noto Sans Bengali"'),
    'ar': ('Noto+Kufi+Arabic:wght@700;800&family=Noto+Sans+Arabic:wght@400;500', '"Noto Kufi Arabic"', '"Noto Sans Arabic"'),
    'ru': ('Unbounded:wght@700;800', 'Unbounded', ''),
}
PONCT = {'fr': (' : ', ', '), 'zh': ('：', '、')}


def cle(x):
    return hashlib.sha1((x[0] + '|' + x[3]).encode('utf-8')).hexdigest()[:10]


def charger(l):
    p = os.path.join(R, 'donnees', 'traductions', l + '.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None


base = json.loads(lire('donnees', 'incidents.json'))
gabarit = lire('template.html')
carte, proj = lire('carte', 'map.json'), lire('carte', 'proj.json')
ui_fr = charger('fr')['ui']
dispo = [l for l in LANGUES if l == 'fr' or charger(l)]
page = lambda l: 'index.html' if l == 'fr' else f'index.{l}.html'

for l in dispo:
    tr = charger(l) if l != 'fr' else {'ui': ui_fr, 'pays': {}, 'faits': {}}
    ui = {**ui_fr, **tr['ui']}
    faits, pays = tr.get('faits', {}), tr.get('pays', {})
    manque = 0
    raw = []
    for x in base:
        f = faits.get(cle(x))
        if l != 'fr' and not f:
            manque += 1
        t, p, n = f if f else (x[3], x[4], x[5])
        raw.append([x[0], x[1], x[2], t, p, n, [g[:4] + [pays.get(g[3], g[3])] for g in x[6]], x[7]])
    T = {k: v for k, v in ui.items() if not k.startswith(('notes_', 'scale_', 'src_li', 'sources_p'))}
    colon, sep = PONCT.get(l, (': ', ', '))
    T.update(lang=l, dir='rtl' if l in RTL else 'ltr', colon=colon, sep=sep)
    fcss, fdisp, fbody = POLICES.get(l, ('', '', ''))
    nav = ' '.join(
        f'<a href="{page(k)}" hreflang="{k}" lang="{k}"' + (' aria-current="page"' if k == l else '') + '>'
        + html.escape((charger(k) or {'ui': ui_fr})['ui'].get('lang_name', k) if k != 'fr' else ui_fr['lang_name']) + '</a>'
        for k in dispo)
    s = gabarit
    for k, v in ui.items():
        if isinstance(v, str):
            s = s.replace('{{' + k + '}}', v.replace('{n}', '<b id="nEv"></b>') if k == 'notes_p1' else v)
    s = (s.replace('{{LANGS}}', nav)
          .replace('__FCSS__', '&family=' + fcss if fcss else '')
          .replace('__FDISP__', fdisp + ',' if fdisp else '')
          .replace('__FBODY__', fbody + ',' if fbody else '')
          .replace('__T__', json.dumps(T, ensure_ascii=False))
          .replace('__MAP__', carte).replace('__PROJ__', proj)
          .replace('__RAW__', json.dumps(raw, ensure_ascii=False, separators=(',', ':'))))
    tete, corps = s.split('<main', 1)
    alt = ''.join(f'<link rel="alternate" hreflang="{k}" href="{page(k)}">' for k in dispo)
    doc = (f'<!doctype html>\n<html lang="{l}" dir="{T["dir"]}">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
           + tete + alt + '\n</head>\n<body>\n<main' + corps + '\n</body>\n</html>\n')
    open(os.path.join(R, page(l)), 'w', encoding='utf-8').write(doc)
    print(f'{page(l)} : {len(doc)//1024} Ko' + (f' ({manque} faits non traduits)' if manque else ''))
