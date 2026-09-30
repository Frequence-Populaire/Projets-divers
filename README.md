# Fréquence Populaire · Projets divers

Ce dépôt public rassemble les projets éditoriaux et de visualisation de données de [Fréquence Populaire](https://www.fpop.media) : cartes, frises, bases de faits, pages interactives.

Chaque projet vit dans son propre dossier et se suffit à lui-même. On y trouve la page publiée, les données qui la nourrissent, les scripts pour la reconstruire et la méthode suivie, de sorte que chacun peut vérifier, réutiliser ou corriger le travail.

## Projets

| Projet | Description |
|---|---|
| [`main-de-washington/`](main-de-washington/) | **La main de Washington.** Carte animée de 3 067 coups d'État, ingérences, interventions, crimes de guerre, sanctions et opérations d'espionnage attribués aux États-Unis dans le monde, de 1900 à septembre 2026. En dix langues. |

## Organisation d'un projet

Chaque dossier suit, autant que possible, la même structure :

```
nom-du-projet/
├── README.md       ce que montre le projet, comment le lire, ses limites
├── index.html      la page à ouvrir dans un navigateur
├── donnees/        les données de référence (JSON, CSV)
├── scripts/        de quoi valider les données et reconstruire la page
└── methode/        la méthode suivie et les consignes de rédaction
```

## Principes

- **Des sources pour chaque fait.** Chaque donnée renvoie à une source consultable.
- **Distinguer l'établi de l'allégué.** Ce qui est reconnu, documenté ou seulement affirmé est signalé comme tel.
- **Des données ouvertes et réutilisables**, dans des formats simples (JSON, CSV), avec des scripts sans dépendance.
- **Une méthode transparente**, y compris quand des outils d'IA ont servi à constituer les données. Le README de chaque projet le précise, avec les limites qui en découlent.

## Contribuer

Les corrections et ajouts sont bienvenus. Ouvrez une *issue* ou une *pull request* en indiquant la source qui appuie la modification.
