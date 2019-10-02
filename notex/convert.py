import pathlib

import pypandoc

import notex


def convert_markdown_to_latex_pdf(filepath: str) -> None:
    try:
        pypandoc.convert_file(
            source_file=filepath,
            to="pdf",
            format="markdown",
            extra_args=("--lua-filter", _get_extract_title_filter_path()),
            encoding="utf-8",
            outputfile=pathlib.Path(filepath).with_suffix(".pdf").as_posix(),
        )
    except RuntimeError as error:
        error_message = str(error)
        if "Title not found" in error_message:
            raise notex.exceptions.MissingTitle(
                "Title not found in {}".format(filepath)
            ) from error
        elif "More than one title found" in error_message:
            raise notex.exceptions.NonUniqueTitle(
                "More than one title found in {}".format(filepath)
            ) from error
        raise notex.exceptions.ConversionError(
            "An error occurred when converting {}".format(filepath)
        ) from error


def _get_extract_title_filter_path() -> pathlib.PosixPath:
    relative_path = "pandoc_filters/extract_title.lua"
    absolute_path = pathlib.Path(__file__).parent / relative_path
    return absolute_path
