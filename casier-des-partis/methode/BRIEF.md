# Brief commun : base « Le casier des partis »

Projet : une animation en barres, année par année de 1945 à 2026, qui compte pour chaque parti politique français le nombre de **condamnations pénales** de ses responsables : atteintes à la probité et délits financiers, mais aussi meurtres, violences, infractions sexuelles, drogue, provocation à la haine et autres crimes et délits. Chaque condamnation fait monter la barre de son parti, et des filtres par type d’infraction recalculent l’animation.

Tu couvres UNE tranche (famille politique et/ou période), définie dans ton message. Reste dans cette tranche : d'autres agents couvrent le reste et les doublons seront supprimés.

## L'unité de compte : une condamnation
Une ligne = **une personne (physique ou morale) condamnée par une décision de justice pénale dans une affaire**. Si trois élus sont condamnés dans le même jugement, cela fait trois lignes. Si une même personne est condamnée dans deux affaires distinctes, cela fait deux lignes. Une même affaire jugée en première instance puis en appel reste UNE ligne (celle de la première condamnation), avec la peine finale et le statut à jour.

## Qui entre
- Ministres, parlementaires (députés, sénateurs, députés européens), présidents de conseil régional ou général, maires, adjoints et conseillers, dirigeants, trésoriers et permanents de partis, collaborateurs directs (assistants parlementaires, directeurs de cabinet, trésoriers de campagne), candidats.
- Les partis eux-mêmes et leurs structures satellites quand ils sont condamnés comme **personnes morales** (micro-partis, associations de financement).
- Les élus locaux de petites communes aussi, s'ils sont bien documentés (presse nationale ou régionale, décision publiée).
- Le parti retenu est **celui de la personne au moment des faits**. Si les faits s'étalent sur un changement de nom, prends le nom en vigueur à la fin des faits. Élu divers droite, divers gauche ou sans étiquette : codes `dvd`, `dvg`, `se`.

## Quelles infractions (`cat`)
- `corr` : corruption active ou passive, trafic d'influence
- `detour` : détournement de fonds publics, emplois fictifs, abus de confiance, complicité ou recel de ces délits
- `favor` : favoritisme (atteinte à l'égalité d'accès aux marchés publics), prise illégale d'intérêts, ingérence
- `financ` : financement illégal de parti ou de campagne, dépassement pénal des comptes de campagne, fausses factures au profit d'un parti
- `abs` : abus de biens sociaux, escroquerie, faux et usage de faux, recel dans un contexte d'affaires
- `fisc` : fraude fiscale, blanchiment, déclarations mensongères à la HATVP
- `elec` : fraude électorale (bourrage d'urnes, faux électeurs, achat de voix)

Et, hors probité :
- `meurtre` : meurtre, assassinat, tentative, complicité
- `violence` : violences volontaires, coups et blessures, séquestration, menaces de mort, violences conjugales
- `sexuel` : viol, agression sexuelle, harcèlement sexuel, atteinte sexuelle sur mineur, exhibition, pédocriminalité
- `drogue` : trafic, détention, usage ou cession de stupéfiants
- `haine` : provocation à la haine ou à la violence, injure ou diffamation raciale, contestation de crime contre l'humanité, apologie de crime ou de terrorisme
- `autre` : tout autre délit ou crime (homicide involontaire, conduite en état d'ivresse ayant blessé, harcèlement moral, rébellion, abus de faiblesse, atteintes à la sûreté de l'État, etc.)

Et, hors pénal :
- `travail` : condamnations prud'homales ou en droit du travail
- `civil` : condamnations civiles, commerciales ou administratives

Une condamnation antérieure à l'entrée en politique entre aussi : code `se` au moment des faits ; l'animation la reporte sur le parti que la personne rejoint ensuite.

- `diffam` : diffamation ou injure simples (non racistes), UNIQUEMENT si la condamnation est définitive (`statut: "def"`)

N'entrent PAS : contraventions, sanctions purement électorales ou administratives (inéligibilité par le Conseil constitutionnel pour un compte de campagne rejeté, sans jugement pénal), condamnations de la Cour de discipline budgétaire, épuration de 1944-1945.

## Ce qui n'entre pas
- Mises en examen, renvois, réquisitions, enquêtes : pas de condamnation, pas de ligne.
- Relaxes et condamnations annulées définitivement (relaxe en appel, cassation sans renvoi) : pas de ligne.
- Faits amnistiés avant tout jugement (loi du 15 janvier 1990, etc.) : pas de ligne.
- Trois états : `statut: "pi"` (condamné en première instance, appel en cours ou possible), `statut: "ap"` (condamnation prononcée ou confirmée en appel, pourvoi en cassation en cours ou possible), `statut: "def"` (définitive : pas d'appel, appel épuisé, cassation rejetée). Condamnation amnistiée après jugement ou dispense de peine : `statut: "def"`, en le disant dans la note.

## Exactitude : la règle d'or
- **Ces lignes nomment des personnes réelles. Une erreur est une diffamation.** N'invente rien. Si tu n'es pas certain qu'une personne a été condamnée, pour quoi et quand, ne l'inclus pas. Mieux vaut 60 lignes sûres que 100 dont 5 fausses.
- Vérifie avec la recherche web tout ce qui n'est pas notoire, et surtout le statut (appel, cassation, relaxe). Les recherches renvoient des extraits : croise-les.
- Dates : `AAAA-MM-JJ` seulement si tu connais le jour du jugement, sinon `AAAA-MM`, sinon `AAAA`. Jamais de « 01 » de remplissage. La date est celle de la **première condamnation** (souvent le tribunal correctionnel).
- Peines : seulement si tu en es sûr. Donne la peine finale si l'affaire a été rejugée, et signale le changement (« 18 mois avec sursis en première instance, 14 mois en appel »).
- Ton neutre de dépêche. Aucun qualificatif moral.

## Format de sortie
Écris un tableau JSON (UTF-8, `ensure_ascii` faux) dans le fichier indiqué dans ton message. Chaque élément :

```json
{
  "date": "2004-01-30",
  "personne": "Alain Juppé",
  "fonction": "secrétaire général du RPR, adjoint au maire de Paris",
  "parti": "rpr",
  "cat": "detour",
  "affaire": "Emplois fictifs du RPR",
  "peine": "18 mois avec sursis et 10 ans d'inéligibilité ; 14 mois avec sursis et 1 an d'inéligibilité en appel (décembre 2004)",
  "statut": "def",
  "note": "Condamné pour prise illégale d'intérêts : des permanents du RPR étaient rémunérés par la Ville de Paris. Le tribunal de Nanterre juge ; la cour d'appel de Versailles réduit la peine.",
  "source": "https://… (URL d'article trouvée par recherche) OU {\"lang\": \"fr\", \"q\": \"Affaire des emplois fictifs de la mairie de Paris\"}"
}
```

- `parti` : un code de la liste ci-dessous, EXACTEMENT.
- `fonction` : la fonction qui explique la condamnation, au moment des faits (80 caractères au maximum).
- `affaire` : nom usuel de l'affaire, 60 caractères au maximum, sans point final.
- `peine` : 200 caractères au maximum.
- `note` : une à deux phrases, 300 caractères au maximum : ce qui est reproché, la juridiction, l'issue.
- `source` : une URL d'article de presse ou de décision trouvée par la recherche web (préférée), sinon un objet de recherche Wikipédia `{"lang","q"}` qui mène à l'article sur l'affaire ou la personne.

### Codes de parti (au moment des faits)
`pcf` · `sfio` · `ps` · `udsr` · `cir` · `psa` · `psu` · `mdc` · `mrc` · `pg` · `gens` (Génération·s) · `lfi` · `verts` · `eelv` · `ecologistes` · `radical` (Parti radical « valoisien ») · `mrg` · `prg` · `mrp` · `cd` (Centre démocrate) · `cds` · `fd` (Force démocrate) · `udf` (UDF sans composante connue, ou Nouvelle UDF 1998-2007) · `modem` · `nc` · `centristes` · `udi` · `cnip` · `ri` · `pr` (Parti républicain, 1977-1997) · `dl` · `rpf47` (RPF gaulliste) · `rs` · `unr` · `udr` · `rpr` · `ump` · `lr` · `rpf99` (RPF de Pasqua) · `mpf` · `dlf` · `agir` · `fn` · `rn` · `mnr` · `reconquete` · `lrem` · `renaissance` · `horizons` · `dvd` · `dvg` · `se` · `ultradroite` · `ultragauche` (groupuscules, onglet « Militants » seulement, avec "militant": true ; nommer le groupe dans `fonction`)

Si un élu UDF appartenait à une composante (PR, CDS, radicaux), donne la composante. Si une personne relève d'un parti absent de la liste, prends `dvd`, `dvg` ou `se` et nomme le parti dans la note.

## Style français
Français correct, accents, guillemets « ». Phrases courtes, voix active. Pas de tirets cadratins.

## Avant de rendre
1. Lance `python3 /home/user/Projets-divers/casier-des-partis/scripts/validate.py <ton fichier>` et corrige jusqu'à obtenir OK.
2. Relis chaque ligne : la condamnation existe-t-elle vraiment ? N'a-t-elle pas été annulée ? Date, parti, statut justes ? Supprime tout ce qui est douteux.

Réponds à la fin avec seulement : le chemin du fichier, le nombre de lignes, et au plus 8 cas que tu as écartés par doute (une ligne chacun).
