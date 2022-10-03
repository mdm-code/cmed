"""Middle English Dictionary Crawler terminal entry point."""

# Standard library imports
import argparse

# Local library imports
from . import Crawler, LAST_MED_ENTRY_ID
from med_crawler.log import CrawlerLogger


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
    parser.add_argument(
        "-l",
        "--log",
        help="log output file",
        default="crawl.log",  # TODO: add date to file name
        type=argparse.FileType("w"),
    )
    parser.add_argument(
        "--requests",
        help="N concurrent requests",
        type=int,
        default=5,
        required=False,
    )
    result = parser.parse_args()
    return result


def crawl(args: argparse.Namespace) -> None:
    c = Crawler(
        output=args.output,
        logger=CrawlerLogger(args.log),
        last_entry_id=args.last_id,
        concurrent_requests=args.requests,
    )
    c.crawl(args.verbose)


def main() -> None:
    args = get_args()
    crawl(args)


if __name__ == "__main__":
    main()
