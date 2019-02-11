# coding=utf-8

import sys
import os
import re
import markdown2
import click


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
def m_t_h(input_file, output_directory, titre):

    ifile = input_file
    path, filename = os.path.split(ifile)
    file_name, file_extension = os.path.splitext(filename)
    link_patterns = [
        (
            re.compile(
                r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)"
            ),
            r"\1",
        )
    ]

    odir = output_directory
    if os.path.exists(odir) == False:
        os.mkdir(odir)
        pass
    else:
        pass

    html_head = (
        '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>'
        + titre
        + "</title>\n</head>\n<body>\n"
    )
    html_foot = "</body>\n</html>"
    md_conv = markdown2.markdown_path(
        ifile, extras=["link-patterns"], link_patterns=link_patterns
    )
    html = html_head + md_conv + html_foot

    f = open("{}{}.html".format(odir, file_name), "w+", encoding="utf-8").write(html)


if __name__ == "__main__":
    m_t_h()
