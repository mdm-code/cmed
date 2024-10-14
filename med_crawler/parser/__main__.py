"""Middle English Dictionary entry parser terminal entry point."""

# Standard library imports
import argparse
import json
from typing import Text
from pathlib import Path
from enum import Enum

# Third-party library imports
from tqdm import tqdm

# Local library imports
from med_crawler.parser import Parser, ParsingStrategy
from med_crawler.parser.db import SqliteMedDB, SqliteMedDbException
from med_crawler.parser.parser import Citation, Entry, Etymology, Form, Pos, Sense


class OutputFormat(str, Enum):
    """Supported parser output formats."""
    JSON = "json"
    SQLITE = "sqlite"

    def __str__(self) -> str:
        return self.name


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Med-parse - Parse MED html dictionary entry data"
    )
    parser.add_argument(
        "-v", "--verbose", help="verbose output", action="store_true"
    )
    parser.add_argument(
        "-d",
        "--dir",
        help="directory with MED XML files",
        type=lambda x: Path(x),
        dest="input_dir",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output file",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--format",
        help="output format",
        choices=[str(fmt).lower() for fmt in OutputFormat],
        type=lambda x: OutputFormat(x.lower()),
        default=OutputFormat.JSON,
    )
    result = parser.parse_args()
    return result


def parse(args: argparse.Namespace) -> None:
    contents: list[Text] = []
    for fname in args.input_dir.iterdir():
        with open(fname, "r") as f:
            contents.append(f.read())
    p = Parser(ParsingStrategy.lxml)
    match args.format:
        case OutputFormat.JSON:
            result = json.dumps(
                [entry.as_dict() for entry in p.parse(contents, args.verbose)]
            )
            with open(args.output, "w") as f:
                f.write(result)
        case OutputFormat.SQLITE:
            entries = p.parse(contents, args.verbose)
            populate_db(args.output, entries)
        case _:
            raise Exception


def populate_db(file_name: str, entries: list[Entry]) -> None:
    try:
        with SqliteMedDB(file_name=file_name) as db:
            db.create_tables()
            entry: Entry
            for entry in tqdm(
                entries,
                desc=f"Writing Middle English Dictionary to {file_name}",
            ):
                db.insert_to_entry_table(entry.as_dto())
                pos: Pos
                for pos in entry.pos:
                    db.insert_to_pos_table(pos.as_dto(entry.id))
                etymology: Etymology
                for etymology in entry.etymologies:
                    db.insert_to_etymology_table(etymology.as_dto(entry.id))
                form: Form
                for form in entry.forms:
                    db.insert_to_form_table(form.as_dto(entry.id))
                sense: Sense
                for sense in entry.senses:
                    db.insert_to_sense_table(sense.as_dto(entry.id))
                citation: Citation
                for citation in entry.citations:
                    db.insert_to_citation_table(citation.as_dto(entry.id))
    except SqliteMedDbException as err:
        raise err


def main() -> None:
    args = get_args()
    parse(args)


if __name__ == "__main__":
    main()
