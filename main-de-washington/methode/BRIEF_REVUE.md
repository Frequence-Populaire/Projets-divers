# Relecture critique d'une base d'incidents

La base recense des ingérences, coups d'État, crimes de guerre, sabotages et opérations d'espionnage attribués aux États-Unis depuis 1900. Elle sera publiée pour un public français. Plusieurs agents l'ont rédigée de mémoire. Ton rôle : vérificateur adversarial. Traque les erreurs.

Pour chaque ligne de ton lot, vérifie :
1. Que le fait existe et que la note est exacte : pas de chiffre, de nom ni de détail inventé.
2. La date. Le format `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ` doit refléter une précision réelle.
3. Le niveau d'attribution `att`, qui porte sur le rôle américain :
   - `a` : reconnu officiellement (opération ouverte, Congrès, justice, archives officielles déclassifiées) ;
   - `s` : documenté par des historiens, des journalistes ou des fuites ;
   - `l` : seulement allégué.
   Un `a` pour un fait qui n'est que documenté est une erreur. Un `a` ou un `s` pour une simple accusation aussi.
4. La catégorie `cat` : coup, arme, crime, mort, sabot, info, espion, cyber.
5. Que le fait relève bien du sujet : un rôle américain, hors du territoire des États-Unis.

N'interviens que si tu es sûr qu'il y a une erreur. Ne touche pas au style.

Écris dans le fichier de sortie indiqué un tableau JSON de corrections :
- `{"id": 12, "action": "drop", "why": "..."}` : le fait est faux, douteux ou hors sujet.
- `{"id": 12, "action": "fix", "set": {"date": "1954-06", "att": "s", "note": "...", "title": "..."}, "why": "..."}` : ne mets que les champs à changer. Titre de 50 caractères au maximum, note de 300 au maximum, en français correct.

Réponds à la fin seulement : le nombre de suppressions, le nombre de corrections, et les trois corrections les plus importantes.
