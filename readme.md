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

- Token
  - [X] Création Token User
  - [X] Refresh

- User
  - [X] Créer un compte
  - [ ] Modifier
  - [ ] Supprimer

- Plateforme
  - [X] Afficher les plateformes
  - [ ] Ajouter
  - [ ] supprimer
  - [ ] modifier

- animes
  - [X] Afficher les animes
  - [X] Ajouter
  - [ ] supprimer
  - [ ] modifier