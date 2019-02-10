# coding=utf-8

import sys
import os
import glob
import markdown2
import click


@click.command()
@click.option(
    "-i",
    "--input-file",
    "input_file",
    default="./robustesse.md",
    help="Chemin vers le fichier Markdown à convertir en HTML. Par défaut le fichier './robustesse.md' est utilisé.",
)
@click.option(
    "-o",
    "--output-directory",
    "output_directory",
    default="./",
    help="Dossier où sera déposé le fichier HTML après conversion. Le chemin vers le dossier doit impérativement se terminer par '\\' par défaut le dossier à la racine du programme est utilisé",
)
@click.option(
    "-t",
    "--titre",
    "titre",
    default="Titre par défaut à changer",
    help="Argument à utiliser pour choisir le titre du fichier HTML",
)
def m_t_h(input_file, output_directory, titre):

    ifile = input_file
    path, filename = os.path.split(ifile)
    file_name, file_extension = os.path.splitext(filename)

    odir = output_directory

    if os.path.exists(ifile) == True and os.path.exists(odir) == True:

        html_head = (
            "<!DOCTYPE html>\n<html>\n<head>\n<title>"
            + titre
            + "</title>\n</head>\n<body>\n"
        )
        html_foot = "</body>\n</html>"
        md_conv = markdown2.markdown_path(ifile)
        html = html_head + md_conv + html_foot

        f = open("{}{}.html".format(odir, file_name), "w+").write(html)

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
