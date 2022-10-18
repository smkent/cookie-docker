from dataclasses import dataclass
from typing import Any, Iterable, List


@dataclass
class ParametrizeParams:
    argnames: Iterable[str]
    argvalues: Iterable[Any]
    ids: Iterable[str]


@dataclass
class ReadmeCase:
    id: str
    argvalues: Iterable[str]


@dataclass
class ReadmeCaseParams:
    id: str
    github_user: str


class ReadmeCases:
    @classmethod
    def all_cases(
        cls,
    ) -> ParametrizeParams:
        argnames = [
            "github_user",
            "expected_content_file",
        ]
        ids: List[str] = []
        argvalues: List[Any] = []
        for case in [
            ReadmeCaseParams(
                id="no_github_user",
                github_user="",
            ),
            ReadmeCaseParams(
                id="github_user",
                github_user="ness",
            ),
        ]:
            ids.append(case.id)
            argvalues.append(
                [
                    case.github_user,
                    f"tests/data/readme-{case.id}.md",
                ]
            )
        return ParametrizeParams(
            argnames=argnames, argvalues=argvalues, ids=ids
        )
