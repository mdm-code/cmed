"""Middle English Dictionary entry parser terminal entry point."""

# Standard library imports
import argparse
import json
from typing import Text

# Local library imports
from med_crawler.parser import Parser, ParsingStrategy


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Med-parse - Parse MED html dictionary entry data"
    )
    parser.add_argument(
        "-v", "--verbose", help="verbose output", action="store_true"
    )
    parser.add_argument(
        "-i",
        "--input",
        help="input file",
        default="-",
        type=argparse.FileType("r"),
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output file",
        default="-",
        type=argparse.FileType("w"),
    )
    result = parser.parse_args()
    return result


def parse(args: argparse.Namespace) -> None:
    htmls: list[Text] = list(
        filter(lambda x: x != "", args.input.read().split("<!DOCTYPE html>"))
    )
    p = Parser(htmls, ParsingStrategy.lxml)
    result = json.dumps([entry.asdict() for entry in p.parse(args.verbose)])
    args.output.write(result)


def main() -> None:
    args = get_args()
    parse(args)


if __name__ == "__main__":
    main()
