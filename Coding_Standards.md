# Coding Standards

## Objectif

Ce document définit les conventions de développement utilisées pour le
projet Portfolio. Elles garantissent la cohérence du code, facilitent la
maintenance et rendent le projet plus lisible.

------------------------------------------------------------------------

# 1. Langue

-   Le code est rédigé en anglais.
-   La documentation est rédigée en français.
-   Les commentaires techniques sont rédigés en français lorsque cela
    améliore la compréhension.

# 2. Nommage des dossiers

-   minuscules uniquement
-   pas d'espaces
-   pas d'accents
-   noms explicites

Exemples :

    core
    articles
    projects
    mountain
    media
    contact
    templates
    static

# 3. Applications Django

Chaque application représente un domaine fonctionnel.

    core
    articles
    projects
    mountain
    media
    contact

# 4. Classes Python

Convention **PascalCase**.

    Article
    Project
    MountainTrip
    Technology
    ContactMessage

# 5. Variables et attributs

Convention **snake_case**.

    created_at
    updated_at
    published_at
    project_name
    article_list

# 6. Constantes

Convention **UPPER_CASE**.

    MAX_UPLOAD_SIZE
    DEFAULT_LANGUAGE

# 7. Templates

    templates/
        base.html
        home.html
        articles/
        projects/
        mountain/
        contact/

# 8. Ressources statiques

    static/
        css/
        js/
        images/
        icons/
        fonts/

# 9. URLs

Toujours en anglais et en minuscules.

    /
    articles/
    projects/
    mountain/
    contact/

# 10. Git

## Branches

    main
    develop
    feature/articles
    feature/projects
    feature/contact
    feature/mountain
    hotfix/...

## Commits

Convention : Conventional Commits.

    feat: create articles application
    fix: correct navbar alignment
    docs: update DDP
    refactor: simplify project views
    style: improve homepage

# 11. Structure documentaire

-   Figures : Figure 1, Figure 2...
-   Tableaux : Tableau 1, Tableau 2...

# 12. Images

Exemples :

    mont_blanc_summit.jpg
    home_banner.webp
    project_dashboard.png

# 13. Bonnes pratiques

-   Une responsabilité par classe.
-   Code lisible avant d'être optimisé.
-   Respect des recommandations PEP 8.
-   Utiliser les fonctionnalités natives de Django avant d'ajouter une
    bibliothèque externe.
-   Tester les fonctionnalités avant chaque commit.

# 14. Évolution

Ce document pourra être complété au fur et à mesure de l'avancement du
projet.
