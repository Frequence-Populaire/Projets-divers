# Assemble la page : gabarit + généalogie des partis + base des condamnations -> index.html
# Usage : python3 scripts/build.py
import os, json

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
lire = lambda *p: open(os.path.join(R, *p), encoding='utf-8').read()

base = json.loads(lire('donnees', 'condamnations.json'))
partis = json.loads(lire('donnees', 'partis.json'))
partis.pop('_lisezmoi', None)
opt = lambda n: json.loads(lire('donnees', n)) if os.path.exists(os.path.join(R, 'donnees', n)) else {}
personnes, mandats = opt('personnes.json'), opt('mandats.json')
personnes.pop('_lisezmoi', None)
mandats.pop('_lisezmoi', None)
CHAMPS = ['date', 'personne', 'fonction', 'parti', 'cat', 'affaire', 'peine', 'statut', 'note', 'source']
raw = [[x[c] for c in CHAMPS] + [1 if x.get('militant') else 0, 1 if x.get('politique') else 0] for x in base]
compact = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))

s = lire('template.html').replace('__PARTIS__', compact(partis)).replace('__RAW__', compact(raw)).replace('__PERSONNES__', compact(personnes)).replace('__MANDATS__', compact(mandats))
tete, corps = s.split('<main', 1)
doc = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       + tete + '</head>\n<body>\n<main' + corps + '\n</body>\n</html>\n')
open(os.path.join(R, 'index.html'), 'w', encoding='utf-8').write(doc)
print(f'index.html : {len(doc) // 1024} Ko, {len(base)} condamnations')
