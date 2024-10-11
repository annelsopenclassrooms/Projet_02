# Projet de scraping de livres

Ce projet est conçu pour extraire l'ensemble des informations des livres du site "Books to Scrape" et enregistrer ces données dans des fichiers CSV, chauqe fichier correspont à une catégorie.
Il recupere egalement les images correspondant aux couvertures de chaque livre.
Le projet est composé de trois scripts.

## Scripts: 

### Book_informations

### Category

### Scrape

## Installation et utilisation

### Prérequis

* Python 3.x
* Modules Python nécessaires : requests, beautifulsoup4, csv

Vous pouvez installer les modules nécessaires en utilisant la commande suivante en bash:
```
pip install requests beautifulsoup4
```

### Utilisation

Pour lancer le scraping, exécutez le script scrape.py. Il va automatiquement scraper toutes les catégories du site "Book to scrape"
```
python scrape.py
```

### Résultats :

Le script va crée deux repertoires

* Extracts: Chaque catégorie a son propre fichier CSV contenant les détails de tous les livres de cette catégorie.
* Images: Les images des couvertures des livres sont téléchargées et enregistrées dans ce dossier.

## Structure du Projet

├── README.md
├── book_information.py  # Gère l'extraction des données spécifiques aux livres
├── category.py          # Gère le scraping des catégories et de la pagination
├── scrape.py            # Script principal pour scraper toutes les catégories et enregistrer les données
├── extracts/            # Dossier où les fichiers CSV seront enregistrés
└── images/              # Dossier où les images des couvertures de livres seront enregistrées

## Axe d'amelioration
