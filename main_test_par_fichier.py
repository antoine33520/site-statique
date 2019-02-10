# coding: utf-8

import sys, os, glob
import markdown2
import click


@click.command()
@click.option(
    "-i",
    "--input-file",
    "input_file",
    default="./markdown/robustesse.md",
    help="Chemin vers le fichier Markdown à convertire en html. Parce défaut le fichier './markdown/robustesse.md' est utilisé.",
)
@click.option(
    "-o",
    "--output-directory",
    "output_directory",
    default="./site/",
    help="Dossier où serra déposé le fichier html après conversion. Le chemin vers le dossier doit impérativement se terminer par '\\' par défaut le dossier utilisé est './site/'",
)
@click.option(
    "-t",
    "--titre",
    "titre",
    default="Titre par défaut à changer",
    help="Argument à utiliser pour choisir le titre du fichier html",
)
# @click.option("-t", "--template-directory", "template_directory", default="", help="")
def m_t_h(input_file, output_directory, titre):

    ifile = input_file
    path, filename = os.path.split(ifile)
    file_name, file_extension = os.path.splitext(filename)
    odir = output_directory

    html_head = (
        "<!DOCTYPE html>\n<html>\n<head>\n<title>"
        + titre
        + "</title>\n</head>\n<body>\n"
    )
    html_foot = "</body>\n</html>"
    md_conv = markdown2.markdown_path(ifile)
    html = html_head + md_conv + html_foot

    f = open("{}{}.html".format(odir, file_name), "w+").write(html)


if __name__ == "__main__":
    m_t_h()
