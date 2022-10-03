"""HTML MED dictionary entry source code parser."""

# Standard library imports
from __future__ import annotations
from dataclasses import dataclass
import enum
import re
from typing import Any, Protocol, Text, TypedDict

# Third-party library imports
from bs4 import BeautifulSoup


__all__ = ["Entry", "Parser", "ParsingStrategy"]


class ParsingException(Exception):
    ...


class BsNode(Protocol):
    def find(self, *args: Any, **kwargs: Any) -> BsNode | str | None:
        raise NotImplementedError

    def find_all(self, *args: Any, **kwargs: Any) -> list[BsNode]:
        raise NotImplementedError

    def get(self, *args: Any, **kwargs: Any) -> str:
        raise NotImplementedError


class EntryDict(TypedDict):
    source_id: str
    headword: str
    pos: str
    forms: list[dict[str, bool | str]]
    citations: list[dict[str, str | None]]


# TODO: rework POS with a dictionary replacement
# TODO: replace unwnted chars in the headword/forms, citations
@dataclass(slots=True, frozen=True, eq=True)
class Entry:
    source_id: str
    headword: str
    _pos: str
    forms: list[Form]
    citations: list[Citation]

    @property
    def pos(self) -> str:
        return self._pos

    def asdict(self) -> EntryDict:
        return {
            "source_id": self.source_id,
            "headword": self.headword,
            "pos": self.pos,
            "forms": [f.asdict() for f in self.forms],
            "citations": [
                c.asdict() for c in self.citations if not c.is_empty()
            ],
        }


@dataclass(slots=True, frozen=True)
class Form:
    head: bool
    form: str

    def asdict(self) -> dict[str, bool | str]:
        return {
            "head": self.head,
            "form": self.form,
        }


@dataclass(slots=True, frozen=True)
class Citation:
    url: str
    date: str
    author: str
    title: str
    ms: str
    scope: str
    text: str

    def is_empty(self) -> bool:
        return not any(
            [
                getattr(self, attr, None)
                for attr in self.__dataclass_fields__.keys()
            ]
        )

    def asdict(self) -> dict[str, str | None]:
        return {
            "url": self.url or None,
            "date": self.date or None,
            "author": self.author or None,
            "title": self.title or None,
            "ms": self.ms or None,
            "scope": self.scope or None,
            "text": self.text or None,
        }


class ParsingStrategy(str, enum.Enum):
    html = HTML = "html.parser"


class Parser:
    def __init__(
        self,
        text: Text,
        strategy: ParsingStrategy = ParsingStrategy.html,
    ) -> None:
        self.soup = BeautifulSoup(text, strategy)

    @property
    def parsed(self) -> list[Entry]:
        entry_regex = re.compile("doc_med.*")
        entries: list[Entry] = []
        for html in self.soup.find_all("div", {"id": entry_regex}):
            entries.append(
                Entry(
                    source_id=self._find_source_id(html),
                    headword=self._find_headword(html),
                    _pos=self._find_pos(html),
                    forms=[Form(*f) for f in self._find_forms(html)],
                    citations=[Citation(**c) for c in self._find_cits(html)],
                )
            )
        return entries

    def _find_source_id(self, elem: BsNode) -> str:
        return elem.get("id").split("_")[-1].upper()

    def _find_headword(self, elem: BsNode) -> str:
        head_node: Any = elem.find("div", {"class": "entry-headword"})
        if not head_node:
            raise ParsingException("failed to detect entry-headword")
        hw: Any = head_node.find(text=True)
        if not hw:
            raise ParsingException("failed to find the entry headword")
        if isinstance(hw, str):
            return hw.strip()
        raise ParsingException("headword is None")

    def _find_pos(self, elem: BsNode) -> str:
        head_node: Any = elem.find("div", {"class": "entry-headword"})
        if not head_node:
            raise ParsingException("failed to detect entry-headword")
        pos: Any = head_node.find("span", {"class": "entry-pos"})
        if not pos:
            raise ParsingException("failed to find the entry POS")
        return pos.text.strip()

    def _find_forms(self, elem: BsNode) -> list[tuple[bool, str]]:
        result: list[tuple[bool, str]] = []
        form_node: Any = elem.find("span", {"class": "FORM"})
        if not form_node:
            raise ParsingException("failed to find the form node")
        head_form: str = form_node.find(
            "span", {"class": "HDORTH"}
        ).text.strip()
        if not head_form:
            raise ParsingException("failed to dectect the headword form")
        result.append((True, head_form))
        forms: list[str] = [
            orth.text.strip()
            for orth in form_node.find_all("span", {"class": "ORTH"}) or []
        ]
        result.extend([(False, f) for f in forms])
        if not result:
            raise ParsingException("failed to find any spelling forms")
        return result

    def _find_cits(self, elem: BsNode) -> list[dict[str, str]]:
        sense_node: Any = elem.find("div", {"class": "senses"})
        if not sense_node:
            raise ParsingException("failed to find the sense node")

        class EmptySpan:
            text: str = ""

        citations: list[dict[str, str]] = [
            {
                "url": (cit.find("a") or {}).get("href", "").strip(),
                "date": (
                    cit.find("span", {"class": "DATE"}) or EmptySpan
                ).text.strip(),
                "author": (
                    cit.find("span", {"class": "AUTHOR"}) or EmptySpan
                ).text.strip(),
                "title": (
                    cit.find("span", {"class": "TITLE"}) or EmptySpan
                ).text.strip(),
                "ms": (
                    cit.find("span", {"clas": "MS"}) or EmptySpan
                ).text.strip(),
                "scope": (
                    cit.find("span", {"class": "SCOPE"}) or EmptySpan
                ).text.strip(),
                "text": (
                    cit.find("span", {"class": "Q"}) or EmptySpan
                ).text.strip(),
            }
            for cit in sense_node.find_all(
                "li", {"class": "citation-list-item"}
            )
        ]
        return citations
