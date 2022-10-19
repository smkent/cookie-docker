# {{ cookiecutter.project_name }}: {{ cookiecutter.project_description }}
{% if cookiecutter.github_user %}
[![Build](https://img.shields.io/github/checks-status/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/main?label=build)][gh-actions]
[![GitHub stars](https://img.shields.io/github/stars/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}?style=social)][repo]
{% endif %}
---

Created from [smkent/cookie-docker][cookie-docker] using
[cookiecutter][cookiecutter]

[cookie-docker]: https://github.com/smkent/cookie-docker
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
{%- if cookiecutter.github_user %}
[gh-actions]: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/actions?query=branch%3Amain
[repo]: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}{% endif %}
