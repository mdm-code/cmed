"""Middle English Dictionary entry parser terminal entry point."""

# Standard library imports
import argparse
import json

# Local library imports
from . import Parser, ParsingStrategy


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
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
    html = args.input.read()
    p = Parser(html, ParsingStrategy.html)
    result = json.dumps([entry.asdict() for entry in p.parsed])
    args.output.write(result)


def main() -> None:
    args = get_args()
    parse(args)


if __name__ == "__main__":
    main()
