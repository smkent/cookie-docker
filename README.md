# [Cookiecutter][cookiecutter] template for new Docker build projects

[![Build](https://img.shields.io/github/checks-status/smkent/cookie-docker/main?label=build)][gh-actions]
[![GitHub stars](https://img.shields.io/github/stars/smkent/cookie-docker?style=social)][repo]

[![cookie-docker][logo]](#)

A template for new Docker build projects for use with GitHub Packages.

## New project creation

### With [cruft][cruft] via script

```python
pip install poetry
poetry install
poetry run new-cookie <path>  # or poetry run cruft create
```

## Development

Prerequisites: [Poetry][poetry-installation]

* Setup: `poetry install`
* Test template rendering and run rendered project tests: `poetry run poe test`
* Fix linting errors: `poetry run poe lint`
* Update test expected output files from test results:
  `poetry run poe updatetests`

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cruft]: https://github.com/cruft/cruft
[gh-actions]: https://github.com/smkent/cookie-docker/actions?query=branch%3Amain
[logo]: https://raw.github.com/smkent/cookie-docker/main/img/cookie-docker.png
[poetry-installation]: https://python-poetry.org/docs/#installation
[repo]: https://github.com/smkent/cookie-docker
