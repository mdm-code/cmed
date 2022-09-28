"""Middle English Dictionary Crawler terminal entry point."""

# Standard library imports
import argparse
import asyncio

# Local library imports
from med_crawler.crawler import Crawler, LAST_MED_ENTRY_ID


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", help="verbose output", action="store_true"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output file",
        default="-",
        type=argparse.FileType("w"),
    )
    parser.add_argument(
        "--last-id",
        help="last MED entry ID",
        type=int,
        default=LAST_MED_ENTRY_ID,
        required=False,
    )
    result = parser.parse_args()
    return result


def parse(args: argparse.Namespace) -> None:
    c = Crawler(args.last_id)
    for page in c.crawl(args.verbose):
        if page.ok:
            args.output.write(page.text)
        else:
            break


def main() -> None:
    args = get_args()
    parse(args)


if __name__ == "__main__":
    main()
