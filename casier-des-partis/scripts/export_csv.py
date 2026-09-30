# Exporte la base en CSV : donnees/condamnations.csv (UTF-8 avec BOM, séparateur virgule).
# Usage : python3 scripts/export_csv.py
import os, csv, json, urllib.parse

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
base = json.load(open(os.path.join(R, 'donnees', 'condamnations.json'), encoding='utf-8'))
partis = json.load(open(os.path.join(R, 'donnees', 'partis.json'), encoding='utf-8'))
CHAMPS = ['date', 'personne', 'fonction', 'parti', 'cat', 'affaire', 'peine', 'statut', 'note']


def source(s):
    return s if isinstance(s, str) else f"https://{s['lang']}.wikipedia.org/w/index.php?search={urllib.parse.quote(s['q'])}"


with open(os.path.join(R, 'donnees', 'condamnations.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(CHAMPS + ['etiquette', 'lignee', 'militant', 'politique', 'source'])
    for x in base:
        w.writerow([x[c] for c in CHAMPS] + [partis['etiquettes'][x['parti']], partis['organisations'][x['parti']],
                    int(bool(x.get('militant'))), int(bool(x.get('politique'))), source(x['source'])])
print(f'donnees/condamnations.csv : {len(base)} lignes')
