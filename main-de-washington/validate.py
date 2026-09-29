import json,sys,re
names=set(open('/tmp/claude-0/-home-user-Projets-divers/2c2e36fd-4fd5-5b62-b93d-547609d72d70/scratchpad/build/countries.txt').read().split('\n'))
CATS={'coup','arme','crime','mort','sabot','info','espion','cyber'}
ok=True
for f in sys.argv[1:]:
    d=json.load(open(f))
    assert isinstance(d,list)
    for i,e in enumerate(d):
        err=[]
        for k in ['date','cat','att','title','place','note','targets','wiki']:
            if k not in e: err.append('champ manquant '+k)
        if err: print(f,i,err); ok=False; continue
        if not re.fullmatch(r'(19\d\d|20[0-2]\d)(-(0[1-9]|1[0-2])(-(0[1-9]|[12]\d|3[01]))?)?',e['date']): err.append('date '+e['date'])
        if e['cat'] not in CATS: err.append('cat '+e['cat'])
        if e['att'] not in ('a','s','l'): err.append('att')
        if len(e['title'])>50: err.append('titre > 50 car.')
        if len(e['note'])>300: err.append('note > 300 car.')
        if not e['targets']: err.append('pas de cible')
        for t in e['targets']:
            if t.get('country') not in names: err.append('pays inconnu '+str(t.get('country')))
            if not (-180<=t.get('lon',999)<=180 and -60<=t.get('lat',999)<=85): err.append('coords')
            if not t.get('fr'): err.append('nom fr manquant')
        w=e['wiki']
        if w.get('lang') not in ('fr','en') or not w.get('q'): err.append('wiki')
        if err: print(f,i,e.get('title'),err); ok=False
    print(f, len(d), 'événements')
print('OK' if ok else 'ERREURS')
