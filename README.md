# mistune-jira

## Development

- `pipenv install --python 3.7`
- `pipenv run python dev.py`
- `pipenv run isort --profile black dev.py && pipenv run black dev.py`

## References

- https://pandoc.org/ + https://pandoc.org/MANUAL.html
- https://github.com/lepture/mistune/tree/v2
- https://github.com/lepture/mistune/issues/319
- https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all
- https://confluence.atlassian.com/doc/confluence-wiki-markup-251003035.html
- https://marketplace.visualstudio.com/items?itemName=denco.confluence-markup
- https://markdown-it.github.io/
- https://lichangwei.github.io/md2c/index.html + https://github.com/lichangwei/md2c
- https://pandoc.org/try/

## Notes

- `pandoc test.md -f markdown -t jira -o test.jira`
- https://pandoc.org/try/?params=%7B%22text%22%3A%22%23+h1+Heading%5Cn%5Cn%23%23+h2+Heading%5Cn%5Cn%23%23%23+h3+Heading%5Cn%5Cn%23%23%23%23+h4+Heading%5Cn%5Cn%23%23%23%23%23+h5+Heading%5Cn%5Cn%23%23%23%23%23%23+h6+Heading%5Cn%22%2C%22to%22%3A%22jira%22%2C%22from%22%3A%22markdown%22%2C%22standalone%22%3Afalse%2C%22embed-resources%22%3Afalse%2C%22table-of-contents%22%3Afalse%2C%22number-sections%22%3Afalse%2C%22citeproc%22%3Afalse%2C%22html-math-method%22%3A%22plain%22%2C%22wrap%22%3A%22auto%22%2C%22highlight-style%22%3A%22pygments%22%2C%22files%22%3A%7B%7D%2C%22template%22%3Anull%7D
- `pipenv install black isort mistune`
- `pipenv --rm`
