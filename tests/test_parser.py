"""Tests of the HTML MED dictionary entry source code parser."""

# Third-party library imports
import pytest

# Local library imports
from .resp import resp_text
from med_crawler.parser import parser


@pytest.mark.parametrize(
    "htmls, want",
    [
        (
            [resp_text],
            [
                parser.Entry(
                    source_id="MED1",
                    headword="ā",
                    _pos="n.(1)",
                    forms=[
                        parser.Form(True, "ā")
                    ],
                    citations=[
                        parser.Citation(
                            url="/m/middle-english-dictionary/bibliography/BIB2677?rid=HYP.733.19981211T105002",
                            date="c1175",
                            author="",
                            title="Orm.",
                            ms="(Jun 1)",
                            scope="16434",
                            text="Þe firrste staff iss nemmnedd A Onn ure Latin spæche.",
                        )
                    ],
                )
            ]
        )
    ]
)
def test_parsing(htmls: list[str], want: list[parser.Entry]) -> None:
    p = parser.Parser(htmls, parser.ParsingStrategy.html)
    have = p.parsed
    assert have == want
