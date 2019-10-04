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


def test_main_without_pandoc(mocker):
    # given
    path = "tests/data/full_metadata.md"
    runner = testing.CliRunner()
    pypandoc_mock = mocker.patch(
        target="pypandoc.convert_file",
        side_effect=OSError(
            "No pandoc was found: either install pandoc and add it "
            "to your PATH or or call pypandoc.download_pandoc(...) or "
            "install pypandoc wheels with included pandoc."
        ),
        autospec=True,
    )

    # when
    with pytest.raises(
        notex.exceptions.PandocNotInstalled, match="^Pandoc not installed$"
    ):
        runner.invoke(cli=notex.commands.main, args=[path], catch_exceptions=False)

    pypandoc_mock.assert_called_once()
