# La main de Washington

Carte animée des coups d'État, ingérences, interventions, crimes de guerre, sabotages, sanctions et opérations d'espionnage attribués aux États-Unis hors de leur territoire, de 1900 à fin septembre 2026.

La base compte **2 788 faits distincts**, un par ligne : on ne met pas « guerre du Vietnam » en une ligne, mais Mỹ Lai, l'opération Phoenix, l'agent orange ou les bombardements secrets du Cambodge chacun sur la sienne.

Le projet reprend la visualisation de [« La guerre grise »](https://claude.ai/artifact/TjNchYmk2id1cEEEBJTgyt), la carte des opérations hybrides russes en Europe (2014-2026), et l'applique aux États-Unis à l'échelle mondiale.

## Ouvrir la carte

Ouvrez `index.html` dans un navigateur. La page est autonome : carte, données et code sont intégrés dans le fichier. Seules les polices viennent de Google Fonts.

Deux sélecteurs, au-dessus de la carte, filtrent la carte, la chronologie et le tableau :

- **Zone**
  - **Monde** : tous les faits.
  - **Europe** : le cadrage de « La guerre grise », avec les seuls faits visant l'Europe.
  - **Alliés** : les faits visant un allié officiel des États-Unis à la date du fait. Sont comptés comme alliés les membres de l'OTAN et de la CEE puis de l'UE, du pacte de Rio, les alliés par traité en Asie-Pacifique et les « alliés majeurs hors OTAN », chacun à partir de son adhésion et jusqu'à son éventuel retrait.
- **Période** : 1900 → 2026, ou 2013 → 2026 (la temporalité de « La guerre grise », élargie à l'année des révélations Snowden).

Le tableau sous la carte se filtre par type et par niveau d'attribution, et se cherche par pays, lieu ou nom d'opération.

## Lire la base

### Catégories

| Code | Catégorie | Faits |
|---|---|---|
| `arme` | Intervention armée, invasion, occupation, bombardement, soutien armé, aide militaire | 728 |
| `sabot` | Sabotage, guerre économique, sanctions, lawfare | 503 |
| `crime` | Crime de guerre, massacre, torture, prison secrète, expérimentation humaine | 472 |
| `info` | Ingérence électorale, financement d'opposition, propagande, faux prétexte, veto | 419 |
| `espion` | Espionnage, surveillance, écoutes | 227 |
| `coup` | Coup d'État, renversement, tentative de renversement | 200 |
| `mort` | Assassinat, complot d'assassinat, enlèvement, restitution extraordinaire | 184 |
| `cyber` | Cyberattaque, porte dérobée, logiciel malveillant | 55 |

### Niveaux d'attribution

Le niveau porte sur le **rôle américain**, pas sur la qualification juridique des faits.

| Code | Niveau | Signification | Faits |
|---|---|---|---|
| `a` | Reconnu | Opération ouverte, ou rôle admis par Washington, établi par le Congrès, une justice, une commission officielle ou des archives officielles déclassifiées | 1 987 |
| `s` | Documenté | Établi par des historiens, des journalistes d'investigation ou des fuites (WikiLeaks, Snowden), sans reconnaissance officielle | 615 |
| `l` | Allégué | Accusation du pays visé ou de tiers, sans preuve publique d'un rôle américain décisif. La note dit qui accuse et si l'accusation est démentie ou contredite | 186 |

Sur la carte, un point plein signale un fait reconnu, un cercle un fait documenté, et un cercle pointillé un fait allégué.

### Ce qui est exclu

- Pour les deux guerres mondiales, les batailles. Seuls les faits controversés sont retenus, comme les bombardements de villes ou Hiroshima et Nagasaki.
- Les actes commis sur le territoire des États-Unis, sauf lorsqu'ils visent un autre pays. Porto Rico, territoire colonial, est traité comme les Philippines de l'époque.
- Les opérations purement britanniques (GCHQ) sans lien documenté avec la NSA.

## Fichiers

```
main-de-washington/
├── index.html              page publiée, générée par scripts/build.py
├── template.html           gabarit de la page (HTML, CSS, JavaScript)
├── donnees/
│   ├── incidents.json      base de référence (voir le format ci-dessous)
│   └── incidents.csv       même base en CSV, générée par scripts/export_csv.py
├── carte/
│   ├── map.json            frontières projetées et simplifiées (Natural Earth, 1:50 m)
│   ├── proj.json           paramètres de la projection Equal Earth
│   └── countries.txt       noms de pays valides pour les cibles
├── sources/                documents sources dépouillés (voir sources/README.md)
├── videos/                 les six vues en vidéo MP4 1920×1080
├── scripts/
│   ├── geo.py              projette les frontières → carte/
│   ├── build.py            assemble index.html
│   ├── validate.py         vérifie la base
│   ├── export_csv.py       exporte la base en CSV
│   └── video.js            enregistre une vue en vidéo 1920×1080
└── methode/
    ├── BRIEF.md            consignes de rédaction et règles d'exactitude
    ├── BRIEF_DOSSIER.md    consignes des dossiers approfondis par pays
    ├── BRIEF_REVUE.md      consignes de relecture critique
    └── BRIEF_SOURCES.md    consignes de dépouillement des documents sources
```

### Format de `donnees/incidents.json`

Tableau d'incidents, triés par date. Chaque incident est un tableau :

```json
["1968-03-16", "crime", "a", "Massacre de Mỹ Lai", "Sơn Mỹ, Vietnam du Sud",
 "Une compagnie de l'armée américaine tue environ 500 civils…",
 [[108.87, 15.18, "Vietnam", "Vietnam du Sud"]],
 "https://fr.wikipedia.org/w/index.php?search=Massacre%20de%20M%E1%BB%B9%20Lai"]
```

1. **date** : `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ`, selon la précision réellement connue.
2. **catégorie** : un des huit codes ci-dessus.
3. **attribution** : `a`, `s` ou `l`.
4. **titre** : 50 caractères au maximum.
5. **lieu** : lieu lisible.
6. **note** : une à deux phrases.
7. **cibles** : `[longitude, latitude, pays tel qu'il figure sur la carte, nom français]`, une entrée par lieu visé.
8. **source** : lien vers l'article ou le document source ; à défaut, une recherche Wikipédia ciblée.

## Modifier et reconstruire

Python 3 suffit, sans dépendance.

```sh
python3 scripts/validate.py     # vérifie dates, catégories, pays, doublons
python3 scripts/build.py        # régénère index.html
python3 scripts/export_csv.py   # régénère donnees/incidents.csv
```

Pour ajouter un fait, insérez une ligne dans `donnees/incidents.json` au bon endroit chronologique, en suivant les règles de `methode/BRIEF.md`, puis relancez les trois commandes.

### Vidéos

Les six vues sont disponibles en MP4 1920×1080 dans `videos/` :

| Vue | 1900 → 2026 | 2013 → 2026 |
|---|---|---|
| Monde | [4 min 05](videos/main-de-washington_monde_1900-2026.mp4) | [2 min 32](videos/main-de-washington_monde_2013-2026.mp4) |
| Europe | [2 min 21](videos/main-de-washington_europe_1900-2026.mp4) | [1 min 05](videos/main-de-washington_europe_2013-2026.mp4) |
| Alliés | [2 min 18](videos/main-de-washington_allies_1900-2026.mp4) | [1 min 05](videos/main-de-washington_allies_2013-2026.mp4) |

Pour les régénérer après une modification de la base :

`scripts/video.js` enregistre chaque vue en vidéo MP4 1920×1080 à 30 images par seconde. Le rendu se fait image par image, avec une horloge virtuelle, si bien que la vidéo reste fluide quelle que soit la machine. Il faut Node.js, [Playwright](https://playwright.dev/) et ffmpeg.

```sh
node scripts/video.js monde long 0 monde_1900-2026.mp4      # Monde, 1900 → 2026
node scripts/video.js europe court 0 europe_2013-2026.mp4   # Europe, 2013 → 2026
node scripts/video.js allies long 0 allies_1900-2026.mp4    # Alliés, 1900 → 2026
```

Le troisième argument fixe la durée en secondes. Avec `0`, elle est calculée à raison de six faits par seconde, entre 1 et 4 minutes, plus 5 secondes d'arrêt sur l'état final.

La géométrie de `carte/` n'a pas à être refaite. Pour la régénérer, récupérez `countries-50m.json` dans le paquet npm [`world-atlas`](https://www.npmjs.com/package/world-atlas) (version 2.0.2), puis :

```sh
python3 scripts/geo.py chemin/vers/countries-50m.json
```

## Méthode et limites

La base a été constituée avec Claude (Anthropic), en plusieurs vagues d'agents :

1. **Balayage** par période et par région.
2. **Dossiers approfondis** : Cuba, Venezuela, Libye, Iran, Irak, Chine, Russie, Corées, Proche-Orient, Afrique, Europe, Amériques, etc.
3. **Recherches en ligne**, avec source pour chaque fait : faits de 2026, trains de sanctions, aide militaire à l'Ukraine, câbles WikiLeaks, documents Snowden.
4. **Dépouillement de documents sources** (dossier `sources/`) : la liste des déploiements du Congressional Research Service (rapport R42738) et les articles Wikipédia « Foreign interventions by the United States » et « United States involvement in regime change ». Chaque fait a été confronté à la base ; 132 faits absents ont été ajoutés.

Chaque vague a été relue par des agents vérificateurs chargés de traquer les erreurs de date, de chiffre ou d'attribution. Les doublons ont été supprimés automatiquement puis à la main.

Limites à connaître :

- **Sélection, pas recensement.** La base se veut aussi large que possible, mais elle se limite à des faits publiquement documentés.
- **Une grande partie a été écrite de mémoire.** Les faits antérieurs à 2025 ont été rédigés à partir des connaissances du modèle, puis relus, sans vérification systématique en ligne. Environ 2 300 faits renvoient à une recherche Wikipédia plutôt qu'à une source primaire. Une vérification humaine reste nécessaire avant toute citation.
- **Les faits de 2026 et les fuites** (WikiLeaks, Snowden) ont été trouvés et sourcés par recherche web, avec un lien direct vers l'article.
- **Dates approximatives.** Quand seuls l'année ou le mois sont connus, la date est donnée à cette précision.

Les corrections sont bienvenues, avec une source à l'appui.

## Sources principales

- Commission Church du Sénat américain, rapport sur les complots d'assassinat (1975)
- Département d'État, *Foreign Relations of the United States* (FRUS)
- National Security Archive, université George-Washington
- Lindsey O'Rourke, *Covert Regime Change* (2018)
- Dov Levin, *Meddling in the Ballot Box* (2020)
- Tim Weiner, *Des cendres en héritage* (2007)
- Parlement européen, rapport sur Echelon (2001)
- Documents WikiLeaks et Snowden, via Le Monde, Der Spiegel, The Guardian, The Intercept, Libération, Mediapart
- Congressional Research Service, *Instances of Use of United States Armed Forces Abroad, 1798-2023* (R42738)
- Wikipédia en anglais : « Foreign interventions by the United States », « United States involvement in regime change », « United States military deployments »
- Presse internationale pour 2025-2026 (liens dans la base)

Fond de carte : [Natural Earth](https://www.naturalearthdata.com/), domaine public, via [world-atlas](https://github.com/topojson/world-atlas).
