# Extraction de faits depuis des sources Wikipédia (projet « La main de Washington »)

Base existante (2 656 faits, 1900 → sept. 2026) : donnees/incidents.json
Format d'une ligne de la base : [date, cat, att, titre, lieu, note, [[lon,lat,paysCarte,nomFr]...], source]

Règles de rédaction et d'exactitude : lis D'ABORD methode/BRIEF.md (catégories, niveaux d'attribution, style en français, titres ≤ 50 caractères, notes ≤ 300 caractères, noms de pays de countries.txt).

## Ta mission
Lire intégralement la tranche de source indiquée, relever CHAQUE fait daté (à partir de 1900, jusqu'à sept. 2026) impliquant une action américaine hors du territoire des États-Unis visant un autre pays : coup, ingérence, intervention armée, bombardement, déploiement de combat, occupation, soutien armé à une rébellion, assassinat ou complot, crime de guerre, sabotage, sanctions, espionnage, propagande, cyber. Un fait = une entrée (ne pas regrouper).

Pour chaque fait candidat, VÉRIFIER qu'il n'est pas déjà dans la base : grep par pays, nom d'opération, personnage, année (ex. `grep -i "guyan" incidents.json`). S'il y est déjà (même événement, même à une date un peu différente), ne pas l'ajouter. Ne garder que les faits nouveaux.

Exclure : secours humanitaires purs, évacuations de ressortissants sans combat, simples visites, faits antérieurs à 1900, faits purement sur le sol américain, opinions d'auteurs sans fait daté.

Attribution : `a` si opération ouverte/reconnue ou établie officiellement ; `s` si documentée par historiens/presse ; `l` si seulement alléguée. Ne pas surqualifier : la source Wikipédia dit souvent « allegedly », « reportedly » → `l` ou `s`.
Dates : précision réellement connue (AAAA, AAAA-MM, AAAA-MM-JJ). N'invente rien ; en cas de doute sur un détail, reste général.

## Sortie
Un fichier JSON (tableau) au chemin indiqué, chaque élément :
{"date":"1968-10","cat":"info","att":"s","title":"…","place":"Ville, Pays","note":"…","targets":[{"lon":..,"lat":..,"country":"<nom exact de countries.txt>","fr":"<nom français>"}],"wiki":{"lang":"en","q":"<requête>"},"url":"https://en.wikipedia.org/wiki/<Article>#<Section_éventuelle>"}
L'url pointe vers l'article source (ou mieux, l'article Wikipédia dédié au fait s'il est cité en lien [[...]] dans le texte : https://en.wikipedia.org/wiki/Titre_avec_underscores).

Valide avec : le validateur du projet  (doit afficher OK).

Réponse finale : nombre de faits ajoutés, et la liste des titres (une ligne chacun), plus les faits écartés comme doublons (compte seulement).
