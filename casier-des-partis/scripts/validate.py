# Vérifie une base de condamnations (format de référence ou format des lots de collecte).
# Usage : python3 scripts/validate.py [fichier.json]   (par défaut donnees/condamnations.json)
import os, re, sys, json

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PARTIS = json.load(open(os.path.join(R, 'donnees', 'partis.json'), encoding='utf-8'))
ORGS = PARTIS['organisations']
CATS = {'corr', 'detour', 'favor', 'financ', 'abs', 'fisc', 'elec', 'meurtre', 'violence', 'sexuel', 'drogue', 'haine', 'autre', 'travail', 'civil', 'diffam'}
STATUTS = {'def', 'ap', 'pi'}
DATE = re.compile(r'^(19[4-9]\d|20[0-2]\d)(-(0[1-9]|1[0-2])(-(0[1-9]|[12]\d|3[01]))?)?$')
LIM = {'fonction': 80, 'affaire': 60, 'peine': 200, 'note': 300}

chemin = sys.argv[1] if len(sys.argv) > 1 else os.path.join(R, 'donnees', 'condamnations.json')
base = json.load(open(chemin, encoding='utf-8'))
err, vus = [], {}
for i, x in enumerate(base):
    if isinstance(x, list):  # format de référence : tableau positionnel
        k = ['date', 'personne', 'fonction', 'parti', 'cat', 'affaire', 'peine', 'statut', 'note', 'source']
        x = dict(zip(k, x))
    ou = f"#{i} {x.get('date')} {x.get('personne')}"
    for c in ('date', 'personne', 'fonction', 'parti', 'cat', 'affaire', 'peine', 'statut', 'note', 'source'):
        if c not in x or x[c] in ('', None):
            err.append(f'{ou} : champ « {c} » manquant')
    if not DATE.match(str(x.get('date', ''))) or str(x.get('date', '')) > '2026-09-30' or str(x.get('date', '')) < '1945':
        err.append(f'{ou} : date invalide')
    if x.get('parti') not in ORGS:
        err.append(f"{ou} : parti inconnu « {x.get('parti')} »")
    if x.get('cat') not in CATS:
        err.append(f"{ou} : catégorie inconnue « {x.get('cat')} »")
    if x.get('statut') not in STATUTS:
        err.append(f"{ou} : statut inconnu « {x.get('statut')} »")
    if x.get('cat') == 'diffam' and x.get('statut') != 'def':
        err.append(f'{ou} : diffamation ou injure simple non définitive (exclue)')
    for c, n in LIM.items():
        if len(str(x.get(c, ''))) > n:
            err.append(f'{ou} : « {c} » dépasse {n} caractères ({len(str(x[c]))})')
    s = x.get('source')
    if isinstance(s, dict):
        if s.get('lang') not in ('fr', 'en') or not s.get('q'):
            err.append(f'{ou} : source Wikipédia mal formée')
    elif not (isinstance(s, str) and s.startswith('http')):
        err.append(f'{ou} : source invalide')
    if '—' in json.dumps(x, ensure_ascii=False):
        err.append(f'{ou} : tiret cadratin')
    cle = (str(x.get('personne', '')).lower(), str(x.get('affaire', '')).lower())
    if cle in vus:
        err.append(f'{ou} : doublon de #{vus[cle]}')
    vus[cle] = i

for e in err:
    print(e)
print('OK' if not err else f'{len(err)} erreur(s)', f'({len(base)} lignes)')
sys.exit(1 if err else 0)
