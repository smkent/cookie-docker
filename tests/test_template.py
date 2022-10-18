import datetime
import os
import subprocess
from typing import Any, Dict

import pytest

from .readme_utils import ReadmeCases

TEMPLATE_ONLY_DATA = "cookiecutter_template_data"


def _bake(cookies: Any, extra_context: Dict[str, Any]) -> Any:
    result = cookies.bake(extra_context=extra_context)

    assert not result.exception
    assert result.exit_code == 0

    assert result.project_path.name == "test-baked-cookie"
    assert result.project_path.is_dir()

    return result


@pytest.mark.parametrize(
    "project_license",
    [
        "GPL-3.0-or-later",
        "GPL-3.0-only",
        "LGPL-3.0-or-later",
        "LGPL-3.0-only",
        "BSD-3-Clause",
        "MIT",
    ],
)
def test_project_license(cookies: Any, project_license: str) -> None:
    result = _bake(
        cookies,
        extra_context=dict(
            author_name="Ness",
            author_email="pk-fire@onett.example.com",
            project_name="test-baked-cookie",
            project_description=(
                'This is a test project called "test-baked-cookie"'
            ),
            project_license=project_license,
        ),
    )

    print(result.project_path)
    print(os.listdir(result.project_path))
    with open(os.path.join(result.project_path, "LICENSE")) as f:
        license_data = f.read()
    with open(
        os.path.join(
            "{{cookiecutter.project_name}}",
            TEMPLATE_ONLY_DATA,
            "licenses",
            project_license,
        )
    ) as f:
        expected_license_data = f.read()

    if project_license in ("MIT", "BSD-3-Clause"):
        # Compare copyright line separately
        if project_license == "MIT":
            expected_copyright = "Copyright (c) {0} Ness".format(
                datetime.date.today().year
            )
        elif project_license == "BSD-3-Clause":
            expected_copyright = "Copyright (c) {0}, Ness".format(
                datetime.date.today().year
            )
        assert license_data.splitlines()[0] == expected_copyright
        license_data = os.linesep.join(license_data.split(os.linesep)[1:])
        expected_license_data = os.linesep.join(
            expected_license_data.split(os.linesep)[1:]
        )

    if project_license == "BSD-3-Clause":
        expected_license_data = expected_license_data.replace(
            "{{ cookiecutter.project_name }}", "test-baked-cookie"
        )

    assert license_data == expected_license_data


def test_rendered_project(cookies: Any) -> None:
    extra_context = dict(
        author_name="Ness",
        author_email="pk-fire@onett.example.com",
        project_name="test-baked-cookie",
        project_description=(
            'This is a test project called "test-baked-cookie"'
        ),
        github_user="ness",
    )
    result = _bake(cookies, extra_context=extra_context)

    assert not (
        subprocess.check_output(
            ["git", "status", "--porcelain=v1"], cwd=result.project_path
        )
        .decode("utf-8")
        .strip()
    ), "Untracked files present in template-rendered project"


@pytest.mark.parametrize(**ReadmeCases.all_cases().__dict__)
def test_rendered_readme(
    cookies: Any,
    github_user: str,
    expected_content_file: str,
    opt_update_expected_outputs: bool,
) -> None:
    result = _bake(
        cookies,
        extra_context=dict(
            author_name="Ness",
            author_email="pk-fire@onett.example.com",
            project_name="test-baked-cookie",
            project_description=(
                'This is a test project called "test-baked-cookie"'
            ),
            github_user=github_user,
        ),
    )

    with open(os.path.join(result.project_path, "README.md"), "r") as f:
        readme = f.read()
    if opt_update_expected_outputs:
        with open(expected_content_file, "w") as f:
            f.write(readme)

    with open(expected_content_file, "r") as f:
        assert readme == f.read()
