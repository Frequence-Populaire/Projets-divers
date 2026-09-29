# Brief commun : base « La main de Washington »

Projet : une carte animée qui recense, pour un public français, les ingérences, coups d'État, interventions, crimes de guerre, sabotages, opérations d'espionnage et autres « sales coups » commis ou soutenus par les États-Unis hors de leur territoire depuis 1900. Le demandeur veut une base **aussi exhaustive que possible**, avec **une ligne par fait distinct**. On ne met pas « guerre du Vietnam » en une ligne : on met Mỹ Lai, l'opération Phoenix, l'agent orange, les bombardements secrets du Cambodge, etc., chacun sur sa propre ligne.

Tu couvres UNE tranche (période et région), définie dans ton message. Reste strictement dans cette tranche : d'autres agents couvrent le reste, et les doublons seront supprimés.

## Ce qui entre
- Coups d'État et renversements, y compris les tentatives et les pressions décisives.
- Interventions armées, invasions, occupations, bombardements, soutien armé à des guérillas ou à des armées répressives, livraisons d'armes clandestines.
- Crimes de guerre et massacres par des forces américaines ou sous commandement américain, bombardements de civils, torture, détentions illégales, expérimentations humaines, essais nucléaires sur des populations, armes chimiques ou incendiaires contre des civils.
- Assassinats, complots d'assassinat, enlèvements, restitutions extraordinaires.
- Sabotages, déstabilisation économique, sanctions aux conséquences humanitaires massives.
- Ingérence électorale, financement d'oppositions, propagande, désinformation, faux prétextes.
- Espionnage et surveillance d'États, d'alliés, de dirigeants, d'institutions et d'entreprises.
- Cyberattaques, portes dérobées, logiciels malveillants.
- Soutien actif à des crimes commis par des alliés (fourniture de listes, feu vert, formation de tortionnaires) : oui, si le rôle américain est documenté ou allégué de façon précise.

Les grandes guerres (Corée, Vietnam, Irak, Afghanistan…) entrent désormais, **éclatées en faits distincts** : chaque massacre, chaque campagne de bombardement notable, chaque programme (Phoenix, Ranch Hand…), chaque mensonge d'État, chaque prison. Pour la Seconde Guerre mondiale, garde uniquement les faits emblématiques et controversés (bombardements de villes, Hiroshima, Nagasaki), pas les batailles.

## Exactitude : la règle d'or
- N'invente rien. Si tu n'es pas sûr qu'un fait existe, ne l'inclus pas. Mieux vaut 80 faits sûrs que 120 dont 10 faux.
- Dates : `AAAA-MM-JJ` seulement si tu connais le jour avec certitude, sinon `AAAA-MM`, sinon `AAAA`. Ne mets jamais un « 01 » de remplissage.
- Chiffres (morts, montants) : seulement si tu en es sûr, sinon « des dizaines », « des centaines », ou rien.
- Pas d'éditorialisation. Des faits, un ton neutre et précis, comme une dépêche. Quand un fait est contesté, dis-le dans la note.

## Niveau d'attribution (`att`) : il porte sur le rôle américain, pas sur la qualification juridique
- `a` = reconnu : opération ouverte ou officielle, ou rôle admis par le gouvernement américain, établi par le Congrès, une justice, une commission officielle ou des archives officielles déclassifiées.
- `s` = documenté : établi par des historiens, des journalistes d'investigation ou des fuites de documents, sans reconnaissance officielle.
- `l` = allégué : accusation du pays visé ou de tiers, sans preuve publique solide d'un rôle américain décisif.

## Catégories (`cat`)
- `coup` : coup d'État, renversement, tentative de renversement
- `arme` : intervention armée, invasion, occupation, bombardement militaire, soutien armé à une guérilla ou à une armée
- `crime` : massacre, crime de guerre, bombardement de civils, torture, prison secrète, expérimentation humaine, essais nucléaires sur des populations
- `mort` : assassinat, complot d'assassinat, enlèvement, disparition ciblée, restitution extraordinaire
- `sabot` : sabotage, déstabilisation ou guerre économique, sanctions meurtrières
- `info` : ingérence électorale, financement d'opposition, propagande, désinformation, faux prétexte
- `espion` : espionnage, surveillance, écoutes
- `cyber` : cyberattaque, porte dérobée, logiciel malveillant

## Format de sortie
Écris un tableau JSON (UTF-8, `ensure_ascii` faux) dans le fichier indiqué dans ton message. Chaque élément :

```json
{
  "date": "1968-03-16",
  "cat": "crime",
  "att": "a",
  "title": "Massacre de Mỹ Lai",
  "place": "Sơn Mỹ, Vietnam du Sud",
  "note": "Une compagnie de l'armée américaine tue environ 500 civils. Le lieutenant William Calley est le seul condamné, puis gracié partiellement.",
  "targets": [{"lon": 108.87, "lat": 15.18, "country": "Vietnam", "fr": "Vietnam du Sud"}],
  "wiki": {"lang": "fr", "q": "Massacre de Mỹ Lai"}
}
```

- `title` : 50 caractères au maximum, en français, sans point final.
- `place` : lieu lisible (« Ville, Pays »).
- `note` : une à deux phrases en français, 300 caractères au maximum, qui disent ce qui s'est passé et d'où vient l'attribution.
- `targets` : un ou plusieurs lieux visés. Prends les coordonnées du lieu précis quand il compte (massacre, base, ville bombardée), sinon celles de la capitale. `country` DOIT être exactement un nom de la liste `countries.txt` (noms anglais de la carte ; URSS → `Russia`, Yougoslavie → `Serbia`, Vietnam du Sud ou du Nord → `Vietnam`). `fr` = nom français du pays à afficher (ex. « Vietnam du Nord », « URSS », « Corée du Sud »).
- `wiki` : requête de recherche Wikipédia qui mène à l'article sur ce fait (`lang` `fr` ou `en`, `q` = titre probable de l'article ou mots-clés précis).

## Style français
Français correct et naturel, avec les accents, des guillemets « » et des espaces insécables inutiles. Phrases courtes, voix active. Pas de tirets cadratins.

## Avant de rendre
1. Lance `python3 validate.py <ton fichier>` et corrige jusqu'à obtenir OK.
2. Relis chaque ligne : existe-t-elle vraiment ? Date, lieu, niveau d'attribution justes ? Supprime tout ce qui est douteux.
3. Tu peux reprendre et corriger les faits de ta tranche qui se trouvent dans `v1_events.json` (version précédente, format tableau : date, cat, att, titre, lieu, note, cibles, lien), en les éclatant si besoin.

Réponds à la fin avec seulement : le chemin du fichier, le nombre de faits, et au plus 5 faits que tu as écartés par doute.
