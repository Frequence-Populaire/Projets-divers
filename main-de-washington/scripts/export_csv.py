# Exporte la base en CSV (une ligne par incident, cibles séparées par « ; »).
# Usage : python3 scripts/export_csv.py
import csv,json,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
base=json.load(open(os.path.join(R,'donnees','incidents.json'),encoding='utf-8'))
LBL={'a':'reconnu','s':'documenté','l':'allégué'}
with open(os.path.join(R,'donnees','incidents.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['date','categorie','attribution','titre','lieu','note','pays_vises','coordonnees','source'])
    for d,c,a,t,pl,n,tg,src in base:
        w.writerow([d,c,LBL[a],t,pl,n,'; '.join(dict.fromkeys(g[3] for g in tg)),'; '.join(f'{g[1]},{g[0]}' for g in tg),src])
print(len(base),'lignes écrites')
