# Anime API

## Modèles

- User

- Plateformes
    - nom
    - url

- animes
    - nom
    - nom original (optionnel)
    - description (optionnel)
    - url
    - nombres_saisons
    - status_anime
    - status
    - image (optionnel)
    - Plateforme (ForeignKey)
    - User (ForeignKey)

## Fonctionnalités

- User
  - [X] Créer un compte
  - [ ] Modifier son compte
  - [ ] Supprimer son compte

- Plateforme
  - [ ] Afficher les plateformes
  - [ ] Ajouter
  - [ ] supprimer
  - [ ] modifier

- animes
  - [X] Afficher les animes
  - [X] Ajouter
  - [ ] supprimer
  - [ ] modifier