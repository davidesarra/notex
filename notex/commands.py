import pathlib

import click

import notex


@click.command(
    help=(
        "Convert markdown files to PDF "
        "(PATH should be the path of the markdown file to convert)"
    )
)
@click.argument("path")
def main(path: str) -> None:
    if pathlib.Path(path).is_file():
        notex.convert.convert_markdown_to_latex_pdf(filepath=path)
    else:
        raise notex.exceptions.FileNotFound(
            "{} does not exist or is not a file".format(path)
        )
