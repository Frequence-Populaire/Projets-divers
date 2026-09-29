# Dossier approfondi

Commence par lire BRIEF.md. Tu y trouveras le format, les catégories, les niveaux d'attribution, les règles d'exactitude et de style, et le validateur.

Le demandeur veut une couverture EXHAUSTIVE de ton dossier, avec une entrée par fait distinct. Chaque complot, chaque tentative, chaque sanction, chaque opération, chaque décret, chaque frappe, chaque accusation formelle a sa propre ligne.

Le fichier `existant_<dossier>.json` liste les faits déjà présents dans la base pour ce pays. Ne les recrée pas. Écris UNIQUEMENT des faits nouveaux et complémentaires. Si un fait existant regroupe plusieurs faits, écris les faits séparés et ajoute le titre exact de la ligne à retirer dans le champ `"remplace"` de l'un d'eux, par exemple `"remplace": "Complots contre Fidel Castro"`. Ce champ est facultatif.

L'exactitude prime sur le nombre. N'écris rien d'inventé. Quand un fait n'est affirmé que par le pays visé (par exemple les « 638 tentatives » revendiquées par Cuba), mets `att` à `l` et dis-le dans la note. Le niveau `a` est réservé à ce qui est officiel : rapport de la commission Church, archives déclassifiées, décisions publiques. Ne mets rien d'après juin 2026. Si tu n'es pas sûr d'un fait de 2025-2026, ne le mets pas.

Lance `python3 validate.py <fichier>` jusqu'à obtenir OK. Le champ supplémentaire `remplace` est toléré.

Réponds à la fin seulement : le chemin du fichier, le nombre de faits, les lignes à remplacer, et au plus 3 faits écartés par doute.
