# -*-coding:utf-8 -*

import sys, os
import markdown2
import click
import re


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
def m_t_h(input_directory, output_directory, titre):

    idir = input_directory
    odir = output_directory

    if os.path.exists(odir) == False:
        os.mkdir(odir)
        pass
    else:
        pass

    if os.path.exists(odir) == False:
        os.mkdir(odir)
        pass
    else:
        pass
    # if os.path.exists(idir) == True and os.path.exists(odir) == True:

    html_head = (
        '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>'
        + titre
        + "</title>\n</head>\n<body>\n"
    )
    html_foot = "</body>\n</html>"

    files = os.listdir(idir)
    i = 0
    for e in idir:
        file_name, file_extension = os.path.splitext(files[i])
        link_patterns = [
            (
                re.compile(
                    r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)"
                ),
                r"\1",
            )
        ]
        md_conv = markdown2.markdown_path(
            idir + files[i], extras=["link-patterns"], link_patterns=link_patterns
        )
        html = html_head + md_conv + html_foot
        f = open("{}{}.html".format(odir, file_name), "w+", encoding="utf-8").write(
            html
        )
        i += 1

    # elif os.path.exists(idir) == True and os.path.exists(odir) == False:
    #     print("Le dossier de destination n'existe pas !")
    # elif os.path.exists(idir) == False and os.path.exists(odir) == True:
    #     print("Le fichier indiqué n'existe pas !")
    # elif os.path.exists(idir) == False and os.path.exists(odir) == False:
    #     print("Le fichier indiqué et le dossier de destination n'existent pas !")
    # else:
    #     pass


if __name__ == "__main__":
    m_t_h()

