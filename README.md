# Projet de scraping de livres

Ce projet est conçu pour extraire l'ensemble des informations des livres du site "Books to Scrape" et enregistrer ces données dans des fichiers CSV, chaque fichier correspond à une catégorie.
Il récupère également les images correspondant aux couvertures de chaque livre.
Le projet est composé de trois scripts.

## Scripts: 

### Book_informations.py

Ce script gère l'extraction des données spécifiques d'un livre à partir de la page d'un livre individuel. Grace à la fonction "get_book_infos", il récupère et organise les informations suivantes :

* product_page_url: L'URL de la page du livre.
* UPC : Code universel de produit.
* title : Le titre du livre.
* price_including_tax : Le prix du livre avec taxes.
* price_excluding_tax : Le prix du livre hors taxes.
* number_available : Nombre de copies en stock.
* product_description : Description du livre.
* category : La catégorie du livre.
* review_rating : La note du livre (de 0 à 5 étoiles).
* image_url : L'URL de la couverture du livre.

Le script comprend également une fonction "download_image" pour télécharger l'image de la couverture du livre localement et une fonction "fill_csv" pour enregistrer les données extraites dans un fichier CSV.

### Category.py

Ce script s'occupe de la gestion des catégories et de la pagination.

Fonctions principales:

* get_url_book_list(category_url) : Récupère toutes les URLs de livres d'une page de catégorie.
* get_category_url_list(category_url) : Gère la pagination et récupère les URLs de toutes les pages d'une catégorie.
* next_page(url) : Vérifie la présence d'une page suivante dans une catégorie et renvoie l'URL si elle existe.

### Scrape.py

Ce script coordonne l'ensemble du processus de scraping.

* Il récupère toutes les catégories disponibles depuis la page d'accueil.
* Pour chaque catégorie, il récupère toutes les URLs de livres sur plusieurs pages (si nécessaire).
* Il extrait les informations de chaque livre à l'aide des fonctions du script book_information.py.
* Il enregistre les données dans des fichiers csv distincts correspondant à une catégorie.

Fonctions principales:

* get_categories(home_url) : Récupère les noms et les URLs des catégories depuis la page d'accueil.
* main() : Fonction principale qui orchestre le scraping de toutes les catégories et enregistre les données dans des fichiers CSV.

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

* Gestion des erreurs
* Meilleurs séparation des différentes étapes d'ETL
* Parallélisation (en attendant les réponses du site)

