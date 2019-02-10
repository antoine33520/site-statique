# -*-coding:utf-8 -*

import sys, os, glob
import markdown2
import click


@click.command()
@click.option(
    "-i",
    "--input-file",
    "input_file",
    default="./markdown/robustesse.md",
    help="Chemin vers le fichier Markdown à convertire en html.",
)
@click.option(
    "-o",
    "--output-directory",
    "output_directory",
    default="./site",
    help="Dossier où serra déposé le fichier html après conversion. Le chemin vers le dossier doit impérativement se terminer par '\\'",
)
# @click.option("-t", "--template-directory", "template_directory", default="", help="")
def m_t_h(input_file, output_directory):

    ifile = input_file
    path, filename = os.path.split(ifile)
    file_name, file_extension = os.path.splitext(filename)
    odir = output_directory

    html = markdown2.markdown_path(ifile)
    print(path)
    print(filename)
    print(file_name)
    print(file_extension)
    print(output_directory)
    f = open("{}{}.html".format(odir, file_name), "w+").write(html)


if __name__ == "__main__":
    m_t_h()
