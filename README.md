# NoTeX

NoTeX is simple CLI application to convert Markdown files into LaTeX-processed
PDF files.

The title of the PDF is taken from the metadata or from the first-level header
(`# Header`).

The LaTeX conversion supports pandoc's [metadata] and [variables] declarations.

For example:

```markdown
---
abstract: This is the abstract.
table-of-contents: true
---

# Title

Introduction.

## Paragraph Header

Paragraph body.
```

## Philosophy

When in 2004 John Gruber [created][md_wiki] the Markdown language, he
[intended][original_md_syntax] the language to be used both to write and read
content, with simplicity in mind.

Since then Markdown has been extended, both in terms of syntax and of content.
In particular, [MathJax] allowed to type formulas thus making Markdown a more
convenient way to write scientific notes when the additional features of LaTeX
were not required.

However, using (complex) formulas made reading Markdown files as they are
written an overly inconvenient task. Sometimes, being able to render Markdown
files into LaTeX-processed files can help strike a compromise between ease of
writing and ease of reading.

Moreover, rendered files enable writers to share their formula-heavy content
with others who might not be familiar with the MathJax syntax.

NoTeX was created to make writing and reading scientific Markdown files easy.

## Installation

Clone the repository, then move into the directory install it.

Whilst in the chosen virtual environment, from the directory where you want to
install NoTeX (it can be used anywhere afterwards), run:

```bash
git clone https://github.com/davidesarra/notex.git &&\
cd notex &&\
pip install -e .
```

NoTeX requires `pandoc`. See the
[installation guide][pandoc_installation_guide] for your OS.

To update NoTeX, from the installation folder run:

```bash
git pull origin master
```

To uninstall NoTeX run:

```bash
pip uninstall notex
```

And remove the installation folder.

## Usage

You can convert Markdown files individually, for example:

```bash
notex notes/machine_learning.md
```

## Implementation

NoTeX is Python CLI application based on [pandoc], another CLI application to
convert between markup file formats, including Markdown and LaTeX. NoTeX
narrows down pandoc's scope so that using it becomes dead-simple, also adding
support for LaTeX titles extracted from Markdown.

## Development

After cloning the repo, install the application including development
requirements.

```bash
make install
```

All Python code is formatted using `black` and linted using `flake8`.

```bash
make format
```

```bash
make lint
```

Both formatting and linting checks are performed within the test suite.

```bash
make test
```

[MathJax]:https://www.mathjax.org/
[md_wiki]:https://en.wikipedia.org/wiki/Markdown
[metadata]:https://pandoc.org/MANUAL.html#metadata-variables
[original_md_syntax]:https://daringfireball.net/projects/markdown/syntax
[pandoc]:https://pandoc.org/
[pandoc_installation_guide]:https://pandoc.org/installing.html
[variables]:https://pandoc.org/MANUAL.html#variables-for-latex
