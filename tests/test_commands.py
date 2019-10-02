import pathlib

import pytest
from click import testing

import notex


@pytest.mark.parametrize(
    "path",
    [
        "tests/data/title_in_body.md",
        "tests/data/title_in_metadata.md",
        "tests/data/full_metadata.md",
    ],
)
def test_main(path):
    # given
    runner = testing.CliRunner()

    # when
    runner.invoke(cli=notex.commands.main, args=[path])

    # then
    assert pathlib.Path(path[:-2] + "pdf").is_file()


@pytest.mark.parametrize(
    "path,error,error_msg_pattern",
    [
        (
            "tests/data/double_title.md",
            notex.exceptions.NonUniqueTitle,
            "^More than one title found in .+$",
        ),
        (
            "tests/data/double_header_title.md",
            notex.exceptions.NonUniqueTitle,
            "^More than one title found in .+$",
        ),
        (
            "tests/data/missing_title.md",
            notex.exceptions.MissingTitle,
            "^Title not found in .+$",
        ),
        (
            "tests/data/non_existing_file.md",
            notex.exceptions.FileNotFound,
            "^.+ does not exist or is not a file$",
        ),
    ],
)
def test_main_with_illegal_markdown(path, error, error_msg_pattern):
    # given
    runner = testing.CliRunner()

    # when
    with pytest.raises(error, match=error_msg_pattern):
        runner.invoke(cli=notex.commands.main, args=[path], catch_exceptions=False)
