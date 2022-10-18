import os
import shutil
import subprocess
from typing import Dict, List

TEMPLATE_ONLY_DATA = "cookiecutter_template_data"


def _run(call: List[str], env: Dict[str, str]) -> None:
    subprocess.run(call, env=env).check_returncode()


# Remove template-only data files
shutil.rmtree(os.path.join(os.getcwd(), TEMPLATE_ONLY_DATA))

# Create empty git repository and add generated files
environ = os.environ.copy()
environ.update(
    dict(
        GIT_AUTHOR_NAME="{{ cookiecutter.author_name }}",
        GIT_AUTHOR_EMAIL="{{ cookiecutter.author_email }}",
        GIT_COMMITTER_NAME="{{ cookiecutter.author_name }}",
        GIT_COMMITTER_EMAIL="{{ cookiecutter.author_email }}",
    )
)

_run(["git", "init", "."], env=environ)

# Set initial branch name to "main"
with open(os.path.join(".git", "HEAD"), "w") as f_ref:
    print("ref: refs/heads/main", file=f_ref)

for call in (
    ["git", "add", "."],
    [
        "git",
        "commit",
        "-m",
        "Create {{ cookiecutter.project_name }}",
    ],
):
    _run(call, env=environ)
