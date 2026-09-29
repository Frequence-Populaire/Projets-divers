# Vérifie la base donnees/incidents.json.
# Chaque incident : [date, catégorie, attribution, titre, lieu, note, cibles, source]
#   date : AAAA, AAAA-MM ou AAAA-MM-JJ selon la précision connue
#   catégorie : coup, arme, crime, mort, sabot, info, espion, cyber
#   attribution : a (reconnu), s (documenté), l (allégué)
#   cibles : [[lon, lat, pays tel qu'il figure sur la carte, nom français], ...]
# Usage : python3 scripts/validate.py
import json,os,re,sys
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
pays=set(open(os.path.join(R,'carte','countries.txt'),encoding='utf-8').read().split('\n'))
base=json.load(open(os.path.join(R,'donnees','incidents.json'),encoding='utf-8'))
CATS={'coup','arme','crime','mort','sabot','info','espion','cyber'}
err=0;vus=set()
for i,e in enumerate(base):
    d,c,a,t,pl,n,tg,src=e;pb=[]
    if not re.fullmatch(r'(19\d\d|20[0-2]\d)(-(0[1-9]|1[0-2])(-(0[1-9]|[12]\d|3[01]))?)?',d): pb.append('date')
    if c not in CATS: pb.append('catégorie')
    if a not in ('a','s','l'): pb.append('attribution')
    if not t or len(t)>50: pb.append('titre')
    if not n or len(n)>320: pb.append('note')
    if not tg or any(g[2] not in pays or not (-180<=g[0]<=180 and -60<=g[1]<=85) for g in tg): pb.append('cibles')
    if not src.startswith('http'): pb.append('source')
    if (d,t) in vus: pb.append('doublon')
    vus.add((d,t))
    if pb: err+=1;print(i,d,t,pb)
print(len(base),'incidents,',err,'en erreur')
sys.exit(1 if err else 0)
