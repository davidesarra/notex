import glob
import pathlib

import pytest


@pytest.fixture(autouse=True)
def remove_pdf_artifacts():
    _remove_pdf_artifacts()
    yield
    _remove_pdf_artifacts()


def _remove_pdf_artifacts():
    pdf_files = glob.glob("tests/data/*.pdf")
    for pdf_file in pdf_files:
        pathlib.Path(pdf_file).unlink()
