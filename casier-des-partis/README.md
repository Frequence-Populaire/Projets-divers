# Le casier des partis

Course de barres animée : pour chaque parti politique français, le nombre de **condamnations en justice** de ses responsables, année par année, de 1945 à septembre 2026. Chaque condamnation fait monter la barre de son parti ; un fil « Au tribunal » affiche les jugements au fur et à mesure.

La base compte **404 condamnations** visant **339 personnes** (physiques ou morales), dont 255 définitives. Chaque ligne renvoie à un article, une décision ou une page de recensement, et a été vérifiée par recherche web.

Le projet reprend la maquette de [« La main de Washington »](../main-de-washington/).

## Ouvrir la page

Ouvrez `index.html` dans un navigateur. La page est autonome : données et code sont intégrés. Seules les polices viennent de Google Fonts.

Version en ligne : https://claude.ai/artifact/Ko7mL2gm4J3XGBfoqfVEEJ

### Trois onglets

| Onglet | Condamnations |
|---|---|
| Responsables politiques | 328 |
| Militants (dont groupuscules) | 42 |
| Condamnations politiques | 34 |

- **Responsables politiques** : ministres, parlementaires, élus locaux, dirigeants, trésoriers et collaborateurs de partis, candidats, et les partis eux-mêmes comme personnes morales.
- **Militants** : militants dont l'appartenance au parti au moment des faits est établie, sans être élus ni cadres. Deux barres y regroupent les groupuscules hors partis, **ultradroite** et **ultragauche**, quand le lien avec le groupe est établi par la justice ou la presse.
- **Condamnations politiques** : condamnations liées à un engagement politique (action contre une guerre, refus de servir, désobéissance civile, atteinte à la sûreté de l'État, action autonomiste), qu'elles visent des élus ou des militants. Elles ne comptent pas dans les deux autres onglets.

### Sélecteurs

- **Infractions** : Toutes · Probité · Meurtre · Violences · Sexuelles · Drogue · Haine · Autres · Prud'hommes, civil · Diffamation.
- **Condamnations** : Toutes · Dès l'appel (confirmées en appel ou définitives) · Définitives.
- **Mesure**
  - *Cumul par parti* : une condamnation reste au parti de la personne au moment des faits. Une condamnation prononcée hors de tout parti est versée au parti que la personne rejoint, à la date où elle le rejoint (Le Pen au FN en 1972, Zemmour à Reconquête en 2021).
  - *Casiers portés* : chaque personne apporte toutes ses condamnations au parti où elle se trouve à l'instant t. Si elle change de parti, son casier la suit ; si elle se retire réellement ou meurt, le compteur baisse. Un bandeau annonce chaque mouvement.
- **Échelle** (onglet « Responsables politiques ») : *Nombre* ou *Pour 100 élus*. En cumul, on divise par les députés et eurodéputés élus depuis 1945 ; en casiers portés, par ceux en fonction. Les partis de moins de 5 élus n'apparaissent pas dans cette vue.
- **Héritage** (mode cumul) : *Oui* ou *Non*, voir la généalogie ci-dessous.

Survolez une barre pour voir l'histoire du parti (et, en casiers portés, les casiers les plus lourds) ; cliquez sur une barre pour filtrer le tableau, sur une carte du fil pour ouvrir sa fiche.

### Trois états de procédure

| Code | État | Barre | Condamnations |
|---|---|---|---|
| `def` | Définitive | pleine | 255 |
| `ap` | Confirmée ou prononcée en appel, pourvoi possible | pleine, liseré jaune | 50 |
| `pi` | Première instance, appel en cours ou possible | voilée, rayée de jaune | 99 |

Une relaxe définitive retire la ligne de la base.

## Ce qu'on compte

**Une unité = une personne, physique ou morale, condamnée dans une affaire.** Trois élus condamnés dans le même jugement comptent trois fois ; une affaire rejugée en appel ne compte qu'une fois, à la date de la première condamnation, avec la peine et l'état à jour. Le parti retenu est celui de la personne au moment des faits (à la fin des faits s'ils s'étalent).

| Code | Infractions | Condamnations |
|---|---|---|
| `corr` | Corruption active ou passive, trafic d'influence | 25 |
| `detour` | Détournement de fonds publics, emplois fictifs, abus de confiance | 104 |
| `favor` | Favoritisme, prise illégale d'intérêts | 47 |
| `financ` | Financement illégal de parti ou de campagne | 24 |
| `abs` | Abus de biens sociaux, escroquerie, faux | 20 |
| `fisc` | Fraude fiscale, blanchiment, déclarations mensongères à la HATVP | 13 |
| `elec` | Fraude électorale | 7 |
| `meurtre` | Meurtre, assassinat, tentative, complicité | 12 |
| `violence` | Violences, y compris conjugales, séquestration, menaces | 28 |
| `sexuel` | Viol, agression ou harcèlement sexuels | 12 |
| `drogue` | Stupéfiants | 1 |
| `haine` | Provocation à la haine, injure ou diffamation raciale, négationnisme, apologie | 14 |
| `diffam` | Diffamation ou injure simples, **seulement si la condamnation est définitive** | 8 |
| `autre` | Autres crimes et délits (homicide involontaire, rébellion, harcèlement moral, atteinte à la sûreté de l'État…) | 65 |
| `travail` | Prud'hommes, droit du travail | 12 |
| `civil` | Condamnations civiles, commerciales ou administratives | 12 |

Ne sont pas comptés : mises en examen et procès en cours, relaxes, condamnations annulées, faits amnistiés avant jugement, sanctions purement électorales ou administratives, épuration de 1944-1945.

### Par parti, onglet « Responsables politiques »

Compte au parti de la personne au moment des faits (mode « Cumul par parti », nom actuel de la lignée) :

| Lignée | Condamnations |
|---|---|
| Divers, sans étiquette | 82 |
| RPF, UNR, UDR, RPR, UMP, LR | 80 |
| FN, RN | 51 |
| SFIO, PS | 40 |
| MRP… UDF, MoDem | 17 |
| En marche, LREM, Renaissance | 15 |
| LFI | 11 |
| RI, PR, Démocratie libérale | 9 |
| PCF | 6 |
| Les Verts, EELV, Les Écologistes | 5 |
| MNR | 3 |
| Reconquête | 3 |
| PRG | 2 |
| Rassemblement pour la France, Union des démocrates et indépendants, Horizons, Parti républicain | 1, 1, 1, 1 |

Ces chiffres reflètent autant la couverture de la base que la réalité (voir les limites) : les procès collectifs du FN (assistants européens, kits de campagne) et du MoDem y sont recensés en entier, ceux du RPR ou du PS (lycées d'Île-de-France, Urba) seulement en partie.

## Généalogie des partis

Elle est décrite dans `donnees/partis.json`.

- **Changement de nom** : même barre, les condamnations se cumulent. Le nom affiché est celui de l'année en cours, les anciens noms apparaissent en petit. SFIO → PS ; RPF → Républicains sociaux → UNR → UDR → RPR → UMP → LR ; FN → RN ; MRP → CD → CDS → Force démocrate → UDF → MoDem ; Les Verts → EELV → Les Écologistes.
- **Scission** : la nouvelle barre hérite du compteur du parti d'origine à la date de la scission (MNR issu du FN en 1999, Parti de gauche issu du PS en 2008, Nouveau Centre issu de l'UDF en 2007…). La part héritée est hachurée. Un parti issu d'une scission n'apparaît que s'il compte au moins une condamnation propre.
- **Fusion** : le compteur du parti absorbé est versé à celui qui l'absorbe (Démocratie libérale dans l'UMP en 2002, CIR dans le PS en 1971).
- **Refondation** : un parti réellement nouveau part de zéro (LFI, En marche, Reconquête, UDI, Horizons).

## Fichiers

```
casier-des-partis/
├── index.html                page publiée, générée par scripts/build.py
├── template.html             gabarit (HTML, CSS, JavaScript)
├── donnees/
│   ├── condamnations.json    base de référence
│   ├── condamnations.csv     même base en CSV, générée par scripts/export_csv.py
│   ├── partis.json           généalogie des partis, couleurs, étiquettes
│   ├── personnes.json        parcours des personnes (partis successifs, retrait, décès)
│   └── mandats.json          sièges de députés et d'eurodéputés par parti et par élection
├── scripts/
│   ├── validate.py           vérifie la base
│   ├── build.py              assemble index.html
│   └── export_csv.py         exporte la base en CSV
└── methode/
    └── BRIEF.md              consignes de collecte et règles d'exactitude
```

### Format de `donnees/condamnations.json`

```json
{
  "date": "2004-01-30",
  "personne": "Alain Juppé",
  "fonction": "secrétaire général du RPR, adjoint au maire de Paris",
  "parti": "rpr",
  "cat": "detour",
  "affaire": "Emplois fictifs du RPR",
  "peine": "…",
  "statut": "def",
  "note": "…",
  "source": "https://…"
}
```

`date` est celle de la première condamnation (`AAAA`, `AAAA-MM` ou `AAAA-MM-JJ` selon la précision connue). `parti` est un code de `partis.json` → `organisations`. `source` est une URL ou une recherche Wikipédia `{"lang", "q"}`. Deux champs facultatifs : `"militant": true` (onglet « Militants ») et `"politique": true` (onglet « Condamnations politiques »).

### Format de `donnees/personnes.json`

`parcours` : liste de `[année décimale, code d'organisation ou null]`, chaque entrée valant jusqu'à la suivante ; `null` = hors de la vie politique. `deces` : date du décès. Les personnes morales portent `"morale": true`.

## Modifier et reconstruire

Python 3 suffit, sans dépendance.

```sh
python3 scripts/validate.py     # vérifie dates, codes, longueurs, doublons, diffamation définitive
python3 scripts/build.py        # régénère index.html
python3 scripts/export_csv.py   # régénère donnees/condamnations.csv
```

## Méthode et limites

La base a été constituée avec Claude (Anthropic), par des agents couvrant chacun une famille politique, une période ou un type d'infraction, puis fusionnée, dédoublonnée et relue :

1. **Collecte par famille politique** (gaullistes, UMP/LR, PS et gauche, PCF et écologistes, centre et libéraux, FN/RN et souverainistes, outre-mer et Corse), de mémoire et par recherche web.
2. **Élargissements** demandés par l'éditeur : violences, infractions sexuelles, haine, diffamation définitive, prud'hommes et civil, partis comme personnes morales, militants, groupuscules, condamnations politiques, période 1945-1993.
3. **Dépouillement de trois recensements publics** : [casier-politique.fr](https://casier-politique.fr/) (fondé sur Wikipédia et Wikidata), [Poligraph](https://poligraph.fr/affaires) et [politicards.fr](https://www.politicards.fr/). Chaque fiche a été confrontée à la base, et son statut mis à jour par une recherche de presse quand la fiche était ancienne.
4. **Parcours des personnes** et **sièges par parti** établis pour les modes « Casiers portés » et « Pour 100 élus » ; décès et changements de parti vérifiés en ligne, sièges vérifiés pour la Ve République et les européennes.
5. **Vérification ligne par ligne** : chaque condamnation a été recherchée dans la presse ou dans une décision ; trois lignes ont été retirées (relaxes), une cinquantaine corrigées (dates, peines, statuts), et chaque ligne renvoie désormais à une source consultable.

Limites à connaître :

- **Sélection, pas recensement.** Seules les condamnations publiquement documentées figurent. Les élus locaux, les procès collectifs (lycées d'Île-de-France, Urba, HLM de Paris) et les années 1945-1990 sont sous-représentés.
- **Un compteur n'est pas un taux, ni un jugement sur un parti.** Le nombre de condamnations dépend de la taille d'un parti, de son nombre d'élus, de son ancienneté au pouvoir, de l'intensité des contrôles à chaque époque, et de la couverture de la base : un procès collectif recensé en entier pèse plus que dix affaires locales manquantes.
- **Avant 1990, peu de condamnations**, et pas seulement faute de données : privilège de juridiction des élus locaux jusqu'en 1993, financement des partis encadré seulement en 1988, amnistie de janvier 1990.
- **Parts d'estimation.** La répartition des sièges au sein des coalitions (UDF, NUPES, NFP, Ensemble, listes européennes communes) et les sièges de la IVe République sont des estimations documentées dans `donnees/mandats.json`. Pour quelques personnes, la date d'entrée dans un parti ou de retrait est approximative.
- **Statuts à date.** L'état des procédures est celui connu fin septembre 2026 ; les procès en appel en cours (MoDem, financement libyen…) le feront évoluer.
- **Des personnes réelles.** Chaque ligne renvoie à sa source : citez la source, pas la base.

Les corrections sont bienvenues, avec une source à l'appui.
