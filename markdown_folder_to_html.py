# -*-coding:utf-8 -*

# Importation des librairies
import os
import markdown2
import click
import re

# Déclaration des commandes pour l'utilisation des arguments en ligne de commande
@click.command()
@click.option(
    "-i",
    "--input-directory",
    "input_directory",
    default="./markdown/",
    help="Chemin vers le dossier contenant le(s) fichier(s) Markdown à convertir en HTML. Le dossier doit se trouver dans la même arborescence que le programme, le chemin contenant les fichiers doit IMPÉRATIVEMENT sur terminer par '\\'. Par défaut le programme utilise le dossier ",
)
@click.option(
    "-o",
    "--output-directory",
    "output_directory",
    default="./site/",
    help="Dossier où sera déposé le fichier HTML après conversion.",
)
@click.option(
    "-t",
    "--titre",
    "titre",
    default="Markdown to HTML",
    help="Argument à utiliser pour choisir le titre des fichiers HTML, sans spécification manuelle le titre 'Markdown to HTML' sera utilisé ! Attention: tous les fichiers convertis auront le même titre !",
)

# Fonction utilisée pour la conversion
def m_t_h(input_directory, output_directory, titre):

    # Déclaration des variables de nom des dossiers en paramètre
    idir = input_directory
    odir = output_directory

    # Vérification de l'existence des fichiers et dossiers fournis en paramètre
    if os.path.exists(idir) == True and os.path.exists(odir) == True:

        # Texte pour le formatage html
        html_head = (
            '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>'
            + titre
            + "</title>\n</head>\n<body>\n"
        )
        html_foot = "</body>\n</html>"

        files = os.listdir(idir)
        i = 0
        for e in idir:
            # Sépation des noms des fichiers et de leurs extensions
            file_name, file_extension = os.path.splitext(files[i])
            # liste des caractères pour la conversion des URLs
            link_patterns = [
                (
                    re.compile(
                        r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)"
                    ),
                    r"\1",
                )
            ]
            # Conversion md vers html
            md_conv = markdown2.markdown_path(
                idir + files[i], extras=["link-patterns"], link_patterns=link_patterns
            )
            # Ajout du formatage html
            html = html_head + md_conv + html_foot

            # Création ou modification puis écriture du markdown converti vers html
            f = open("{}{}.html".format(odir, file_name), "w+", encoding="utf-8").write(
                html
            )
            i += 1

    # Erreurs
    elif os.path.exists(idir) == True and os.path.exists(odir) == False:
        print("Le dossier de destination n'existe pas !")
    elif os.path.exists(idir) == False and os.path.exists(odir) == True:
        print("Le fichier indiqué n'existe pas !")
    elif os.path.exists(idir) == False and os.path.exists(odir) == False:
        print("Le fichier indiqué et le dossier de destination n'existent pas !")
    else:
        pass


if __name__ == "__main__":
    m_t_h()

