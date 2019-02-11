# Convertisseur de fichiers Mardowns en fichiers HTML

## I - Description

Ce programme est un convertisseur de fichiers Markdowns en fichiers HTML écrit en python3 pour un projet de cours de première année dans le cadre de mes études à Ynov Informatique.

## II - Prérequis

Pour l'utilisation de ce programme il faut :

- Python 3.7 (testé sur Python 3.7.1)

- Les librairie :
  - Click
    - pip install click (Windows)
    - pip3 install click (Linux)
    - [Lien vers Click](https://pypi.org/project/markdown2/)
  - Markdown2
    - pip install markdown2 (Windows)
    - pip3 install markdown2 (Linux)
    - [Lien vers Markdown2](https://pypi.org/project/markdown2/)

## III - Fonctionnement

Utilisation du programme

`markdown_file_to_html.py` :

Windows:

```powershell
python markdown_file_to_html.py --input-file ./dossier/fichier_markdown --output-directory ./dossier_resultat/ --titre votre_titre
```

Linux:

```bash
python3.7 markdown_file_to_html.py --input-file ./dossier/fichier_markdown --output-directory ./dossier_resultat/ --titre votre_titre
```

`markdown_folder_to_html.py` :

```powershell
python markdown_folder_to_html.py --input-directory ./dossier/fichier_markdown --output-directory ./dossier_resultat/ --titre votre_titre
```

Linux:

```bash
python3.7 markdown_folder_to_html.py --input-directory ./dossier/fichier_markdown --output-directory ./dossier_resultat/ --titre votre_titre
```

## IV - Spécifications

Ce dépôt contient quatres programmes python :

- **markdown_file_to_html.py**
  Permet la conversion d'un fichier markdown vers un fichier html dans le dossier de destination indiqué.
  Il existe une autre version du fichier "main_test_par_fichier.py" qui est la version de test de la version stable. Cette version peut possiblement contenir des modifications non présente dans la version stable.

- **markdown_folder_to_html.py**
  Permet la conversion de tous les fichiers markdown contenu dans un dossier vers des fichiers html dans le dossier de destination indiqué.
  Il existe une autre version du fichier "main_test_par_dossier.py qui est la version de test de la version stable. Cette version peut possiblement contenir des modifications non présente dans la version stable.
