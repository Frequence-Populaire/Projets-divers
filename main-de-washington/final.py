import json,os
from urllib.parse import quote
r=json.load(open('events3.json'))
def conv(e):
    w=e['wiki']
    if e.get('url'): return [e['date'],e['cat'],e['att'],e['title'],e['place'],e['note'],[[t['lon'],t['lat'],t['country'],t['fr']] for t in e['targets']],e['url']]
    return [e['date'],e['cat'],e['att'],e['title'],e['place'],e['note'],[[t['lon'],t['lat'],t['country'],t['fr']] for t in e['targets']],
            'https://%s.wikipedia.org/w/index.php?search=%s'%(w['lang'],quote(w['q']))]
# lignes découpées par l'agent
rm=set();add=[]
if os.path.exists('review/splits.json'):
    for s in json.load(open('review/splits.json')):
        rm.add(s['replace_id']); add+= [conv(e) for e in s['new']]
add=[x for x in add if not any(k in x[3]+x[5] for k in ('Alstom','Pierucci','Lava Jato'))]
out=[x for i,x in enumerate(r) if i not in rm and x[3] not in ("Lava Jato et la justice américaine","Affaire Alstom")]
out+=add+[conv(e) for f in ('parts/Y_bresil_lavajato.json','parts/X_lawfare.json','parts/W_commerce_2018_2026.json','parts/V_allies_armement.json','parts/U_canada.json','parts/T_mexique.json','parts/S_2026_web.json','parts/R_sanctions_aide.json','parts/Q_wikileaks.json','parts/P_snowden.json','parts/O_iran2026.json') for e in (json.load(open(f)) if os.path.exists(f) else [])]
out.sort(key=lambda x:x[0])
json.dump(out,open('events_final.json','w'),ensure_ascii=False,separators=(',',':'))
print(len(rm),'lignes découpées ->',len(add),'faits ;',len(out),'au total')

# ---- dossiers approfondis ----
import glob
out=json.load(open('events_final.json'))
rem=set();new=[]
for f in sorted(glob.glob('dossiers/*.json')+glob.glob('dossiers2/*.json')):
    if 'existant_' in f: continue
    for e in json.load(open(f)):
        if e.get('remplace'): rem.add(e['remplace'])
        new.append(conv(e))
titles={x[3] for x in out}
miss=[t for t in rem if t not in titles]
if miss: print('remplacements introuvables :',miss)
out=[x for x in out if x[3] not in rem]+new
out.sort(key=lambda x:x[0])
json.dump(out,open('events_final.json','w'),ensure_ascii=False,separators=(',',':'))
print('dossiers :',len(new),'faits ajoutés,',len(rem),'lignes remplacées ;',len(out),'au total')

# ---- doublons résiduels ----
DUP={("1967-10-09","Exécution de Che Guevara"),("1996-08-05","Loi D'Amato contre l'Iran et la Libye"),("2025-10-16","Frappe sur un semi-submersible"),("2025-10","Deux Trinidadiens tués en mer")}
out=[x for x in json.load(open('events_final.json')) if (x[0],x[3]) not in DUP]
json.dump(out,open('events_final.json','w'),ensure_ascii=False,separators=(',',':'))
print('après doublons :',len(out))

# ---- doublons de la troisième vague ----
DROP2={("1948","Opération Bloodstone"),("1964","Subvention de la CIA au dalaï-lama"),("1994-04","Feu vert aux armes iraniennes pour la Bosnie"),
("1995-08-04","Opération Tempête en Krajina"),("1996-03-12","La loi Helms-Burton vise les Européens"),("1996-08-05","Loi d'Amato contre Total en Iran"),
("1999","La CIA soutient l'UÇK"),("1999-04-14","Convoi de réfugiés de Djakovica"),("2003-12-31","Enlèvement de Khaled el-Masri"),
("2005","Site noir de la CIA en Lituanie"),("2017","UC Global espionne Assange"),("2017","Plans de la CIA contre Assange à Londres"),
("2024-02-02","Représailles après la Tour 22"),("2025-02-06","Sanctions contre la CPI et son procureur")}
out=json.load(open('events_final.json'));seen=set();res=[]
for x in out:
    k=(x[0],x[3])
    if k in DROP2 or k in seen: continue
    seen.add(k);res.append(x)
json.dump(res,open('events_final.json','w'),ensure_ascii=False,separators=(',',':'))
print('après doublons 2 :',len(res))

# ---- corrections de la relecture des vagues 2 et 3 ----
IDX={'date':0,'cat':1,'att':2,'title':3,'place':4,'note':5}
out=json.load(open('events_final.json'));byk={x[0]+'|'+x[3]:x for x in out};drop=set();nf=0;miss=0
for f in sorted(glob.glob('review2/fix*.json')):
    for c in json.load(open(f)):
        k=c.get('key');x=byk.get(k)
        if x is None: miss+=1;continue
        if c['action']=='drop': drop.add(k)
        else:
            for a,v in c.get('set',{}).items():
                if a in IDX: x[IDX[a]]=v;nf+=1
out=[x for x in out if x[0]+'|'+x[3] not in drop and x[1] in ('coup','arme','crime','mort','sabot','info','espion','cyber') and x[2] in ('a','s','l')]
out.sort(key=lambda x:x[0])
json.dump(out,open('events_final.json','w'),ensure_ascii=False,separators=(',',':'))
print('relecture 2 :',len(drop),'suppressions,',nf,'champs corrigés,',miss,'clés introuvables ;',len(out),'faits')
