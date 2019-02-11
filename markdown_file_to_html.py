# coding=utf-8

# Importation des librairies
import os
import re
import markdown2
import click

# Déclaration des commandes pour l'utilisation des arguments en ligne de commande
@click.command()
@click.option(
    "-i",
    "--input-file",
    "input_file",
    default="./markdown/robustesse.md",
    help="Chemin vers le fichier Markdown à convertir en HTML. Par défaut le fichier './robustesse.md' est utilisé.",
)
@click.option(
    "-o",
    "--output-directory",
    "output_directory",
    default="./",
    help="Dossier où sera déposé le fichier HTML après conversion. Le chemin vers le dossier doit impérativement se terminer par '\\' par défaut le dossier à la racine du programme est utilisé.",
)
@click.option(
    "-t",
    "--titre",
    "titre",
    default="Markdown to HTML",
    help="Argument à utiliser pour choisir le titre du fichier HTML, sans spécification manuelle le titre 'Markdown to HTML' sera utilisé.",
)

# Fonction utilisée pour la conversion
def m_t_h(input_file, output_directory, titre):

    # Déclaration des variables utilisées pour les conversions
    ifile = input_file
    # Sépation du répertoire et du nom du fichier
    path, filename = os.path.split(ifile)
    # Sépation des noms des fichiers et de leurs extensions
    file_name, file_extension = os.path.splitext(filename)
    # liste des caractères pour la conversion des URLs
    link_patterns = [
        (
            re.compile(
                r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)"
            ),
            r"\1",
        )
    ]
    odir = output_directory

    # Vérification de l'existence des fichiers et dossiers fournis en paramètre
    if os.path.exists(ifile) == True and os.path.exists(odir) == True:

        # Texte pour le formatage html
        html_head = (
            '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>'
            + titre
            + "</title>\n</head>\n<body>\n"
        )
        html_foot = "</body>\n</html>"

        # Conversion md vers html
        md_conv = markdown2.markdown_path(
            ifile, extras=["link-patterns"], link_patterns=link_patterns
        )
        # Ajout du formatage html
        html = html_head + md_conv + html_foot

        # Création ou modification puis écriture du markdown converti vers html
        f = open("{}{}.html".format(odir, file_name), "w+", encoding="utf-8").write(
            html
        )

    # Erreurs
    elif os.path.exists(ifile) == True and os.path.exists(odir) == False:
        print("Le dossier de destination n'existe pas !")
    elif os.path.exists(ifile) == False and os.path.exists(odir) == True:
        print("Le fichier indiqué n'existe pas !")
    elif os.path.exists(ifile) == False and os.path.exists(odir) == False:
        print("Le fichier indiqué et le dossier de destination n'existent pas !")
    else:
        pass


if __name__ == "__main__":
    m_t_h()
