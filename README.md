# NoTeX

NoTeX is simple CLI application to convert markdown files into LaTeX-processed
files.

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

NoTeX was created to make writing and reading scientific Markdown files
accessible and simple.

[MathJax]:https://www.mathjax.org/
[md_wiki]:https://en.wikipedia.org/wiki/Markdown
[original_md_syntax]:https://daringfireball.net/projects/markdown/syntax
