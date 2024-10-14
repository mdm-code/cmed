"""HTML MED dictionary entry source code parser."""

# Standard library imports
from __future__ import annotations
from dataclasses import dataclass
import enum
from functools import partial
import multiprocessing
from typing import Any, Text, TypedDict
from uuid import uuid4

# Third-party library imports
from bs4 import BeautifulSoup
from tqdm import tqdm


__all__ = ["Entry", "Parser", "ParsingStrategy"]


class ParsingException(Exception):
    ...


@dataclass
class Entry:
    source_id: str
    headword: Form
    pos: list[Pos]
    etymologies: list[Etymology]
    forms: list[Form]
    senses: list[Sense]
    citations: list[Citation]

    class DTO(TypedDict):
        id: str
        source_id: str
        lemma_regular: str
        lemma_original: str

    class Dict(TypedDict):
        id: str
        source_id: str
        headword: Form.Dict
        pos: list[Pos.Dict]
        etymologies: list[Etymology.Dict]
        forms: list[Form.Dict]
        senses: list[Sense.Dict]
        citations: list[Citation.Dict]

    def __post_init__(self) -> None:
        self._uuid = uuid4()

    @property
    def id(self) -> str:
        return str(self._uuid)

    def as_dict(self) -> Dict:
        headword = self.headword.as_dict()
        del headword["id"]
        return {
            "id": self.id,
            "source_id": self.source_id,
            "headword": headword,
            "pos": [p.as_dict() for p in self.pos],
            "etymologies": [e.as_dict() for e in self.etymologies],
            "forms": [f.as_dict() for f in self.forms],
            "senses": [s.as_dict() for s in self.senses],
            "citations": [
                c.as_dict() for c in self.citations if not c.is_empty()
            ],
        }

    def as_dto(self) -> DTO:
        return self.DTO(
            id=self.id,
            source_id=self.source_id,
            lemma_regular=self.headword.regular,
            lemma_original=self.headword.original,
        )


@dataclass
class Form:
    headword: bool
    regular: str
    original: str

    class DTO(TypedDict):
        id: str
        entry_id: str
        form_regular: str
        form_original: str

    class Dict(TypedDict, total=False):
        id: str
        headword: bool
        regular: str
        original: str


    def __post_init__(self) -> None:
        self._uuid = uuid4()

    @property
    def id(self) -> str:
        return str(self._uuid)

    def as_dict(self) -> Dict:
        return {
            "id": self.id,
            "headword": self.headword,
            "regular": self.regular,
            "original": self.original,
        }

    def as_dto(self, entry_id: str) -> DTO:
        return self.DTO(
            id=self.id,
            entry_id=entry_id,
            form_regular=self.regular,
            form_original=self.original,
        )


@dataclass
class Pos:
    code: str
    code_abbrev: str

    class DTO(TypedDict):
        id: str
        entry_id: str
        code: str
        code_abbrev: str | None

    class Dict(TypedDict):
        id: str
        code: str
        code_abbrev: str | None

    def __post_init__(self) -> None:
        self._uuid = uuid4()

    @property
    def id(self) -> str:
        return str(self._uuid)

    def as_dict(self) -> Dict:
        return {
            "id": self.id,
            "code": self.code,
            "code_abbrev": self.code_abbrev or None,
        }

    def as_dto(self, entry_id: str) -> DTO:
        return self.DTO(
            id=self.id,
            entry_id=entry_id,
            code=self.code,
            code_abbrev=self.code_abbrev or None,
        )


@dataclass
class Etymology:
    code: str
    code_abbrev: str

    class DTO(TypedDict):
        id: str
        entry_id: str
        code: str
        code_abbrev: str | None

    class Dict(TypedDict):
        id: str
        code: str
        code_abbrev: str | None

    def __post_init__(self) -> None:
        self._uuid = uuid4()

    @property
    def id(self) -> str:
        return str(self._uuid)

    def as_dict(self) -> Dict:
        return {
            "id": self.id,
            "code": self.code,
            "code_abbrev": self.code_abbrev or None,
        }

    def as_dto(self, entry_id: str) -> DTO:
        return self.DTO(
            id=self.id,
            entry_id=entry_id,
            code=self.code,
            code_abbrev=self.code_abbrev or None,
        )


@dataclass
class Sense:
    text: str

    class DTO(TypedDict):
        id: str
        entry_id: str
        text: str

    class Dict(TypedDict):
        id: str
        text: str

    def __post_init__(self) -> None:
        self._uuid = uuid4()

    @property
    def id(self) -> str:
        return str(self._uuid)

    def as_dict(self) -> Dict:
        return {
            "id": self.id,
            "text": self.text,
        }

    def as_dto(self, entry_id: str) -> DTO:
        return self.DTO(
            id=self.id,
            entry_id=entry_id,
            text=self.text,
        )


@dataclass
class Citation:
    date: str
    author: str
    title: str
    ms: str
    scope: str
    text: str
    reference: str

    class DTO(TypedDict):
        id: str
        entry_id: str
        date: str | None
        author: str | None
        title: str | None
        manuscript: str | None
        scope: str | None
        text: str
        reference: str | None


    class Dict(TypedDict):
        id: str
        date: str | None
        author: str | None
        title: str | None
        manuscript: str | None
        scope: str | None
        text: str
        reference: str | None

    def __post_init__(self) -> None:
        self._uuid = uuid4()

    @property
    def id(self) -> str:
        return str(self._uuid)

    def is_empty(self) -> bool:
        return not any(
            [
                getattr(self, attr, None)
                for attr in self.__dataclass_fields__.keys()
            ]
        )

    def as_dict(self) -> Dict:
        return self.Dict(
            id=self.id,
            date=self.date or None,
            author=self.author or None,
            title=self.title or None,
            manuscript=self.ms or None,
            scope=self.scope or None,
            text=self.text,
            reference=self.reference or None,
        )

    def as_dto(self, entry_id: str) -> DTO:
        return self.DTO(
            id=self.id,
            entry_id=entry_id,
            date=self.date or None,
            author=self.author or None,
            title=self.title or None,
            manuscript=self.ms or None,
            scope=self.scope or None,
            text=self.text,
            reference=self.reference or None,
        )


class EmptySpan:
    text: str = ""


class ParsingStrategy(str, enum.Enum):
    html = HTML = "html.parser"
    lxml = LXML = "lxml"


class Parser:
    def __init__(
        self,
        strategy: ParsingStrategy = ParsingStrategy.lxml,
    ) -> None:
        self.strategy = strategy

    def parse(
        self, contents: list[Text], verbose: bool = False
    ) -> list[Entry]:
        entries: list[Entry] = []

        if not contents:
            return entries

        n_cpus = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(processes=n_cpus - 1 if n_cpus > 1 else 1)

        if verbose:
            iter = tqdm(
                pool.imap_unordered(
                    partial(parse_single, strategy=self.strategy), contents
                ),
                total=len(contents),
                desc="Parsing Middle English Dictionary",
            )
            entries.extend(list(iter))
        else:
            entries.extend(
                pool.imap_unordered(
                    partial(parse_single, strategy=self.strategy), contents
                )
            )
        return entries


def parse_single(content: Text, strategy: ParsingStrategy) -> Entry:
    soup = BeautifulSoup(content, strategy)
    result = Entry(**Extract(soup)())
    return result


class Extract:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup

    def __call__(self) -> dict[str, Any]:
        result = {
            "source_id": self._find_source_id(),
            "headword": self._find_headword(),
            "pos": self._find_pos(),
            "etymologies": self._find_etymologies(),
            "forms": self._find_forms(),
            "senses": self._find_senses(),
            "citations": self._find_citations(),
        }
        return result

    def _find_source_id(self) -> str:
        node: Any = self.soup.find("entryfree")
        return node["id"]

    def _find_headword(self) -> Form:
        head_node: Any = self.soup.find("hdorth")
        return Form(
            headword=True,
            regular=head_node.find("reg").text.strip(),
            original=(head_node.find("orig") or EmptySpan()).text.strip(),
        )

    def _find_pos(self) -> list[Pos]:
        head_node: Any = self.soup.find("pos")
        result: list[Pos] = []
        for ps in head_node.find_all("ps"):
            result.append(
                Pos(
                    code=ps["expan"].lower().strip(),
                    code_abbrev=ps.text.lower().strip(),
                )
            )
        return result

    def _find_forms(self) -> list[Form]:
        result: list[Form] = []
        head_node: Any = self.soup.find("hdorth")
        result.append(
            Form(
                headword=True,
                regular=head_node.find("reg").text.strip(),
                original=(head_node.find("orig") or EmptySpan()).text.strip(),
            )
        )
        for ort in self.soup.find_all("orth"):
            result.append(
                Form(
                    headword=False,
                    regular=ort.find("reg").text.strip(),
                    original=(
                        head_node.find("orig") or EmptySpan()
                    ).text.strip(),
                )
            )
        return result

    def _find_etymologies(self) -> list[Etymology]:
        etymologies: list[Etymology] = []
        etym_node: Any = self.soup.find("etym")
        if etym_node:
            for etym in etym_node.find_all("lang"):
                etymologies.append(
                    Etymology(
                        code=(etym.find("lg") or {})
                        .get("expan", "")
                        .lower()
                        .strip(),
                        code_abbrev=(etym.find("lg") or EmptySpan)
                        .text.lower()
                        .strip(),
                    )
                )
        return etymologies

    def _find_senses(self) -> list[Sense]:
        head_node: Any = self.soup.find("sense")
        senses: list[Sense] = []
        if head_node:
            for sense in head_node.find_all("def"):
                senses.append(
                    Sense(
                        text=sense.text.strip(),
                    )
                )
        return senses

    def _find_citations(self) -> list[Citation]:
        citations: list[Citation] = []
        for cit in self.soup.find_all("cit"):
            citations.append(
                Citation(
                    date=(cit.find("date") or EmptySpan).text.strip(),
                    author=(cit.find("author") or EmptySpan).text.strip(),
                    title=(cit.find("title") or EmptySpan).text.strip(),
                    ms=(cit.find("ms") or EmptySpan).text.strip(),
                    scope=(cit.find("scope") or EmptySpan).text.strip(),
                    text=(
                        _remove_mulitple_whitespace(
                            (cit.find("q") or EmptySpan)
                            .text.strip()
                            .replace("|", "")
                        )
                    ),
                    reference=(cit.find("stncl") or {}).get("rid", ""),
                )
            )
        return citations


def _remove_mulitple_whitespace(text: str) -> str:
    """Remove multiple whitespace characters from text."""
    return " ".join(text.split())
