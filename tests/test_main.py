"""Tests of the cmed command-line interface entry point."""

# Standard library imports
import argparse
from contextlib import nullcontext as does_not_raise
from io import StringIO

# Local library imports
from med_crawler.crawler import __main__ as cmain
from med_crawler.parser import __main__ as pmain
from .resp import MockResp, resp_string_io


def test_crawl_main(mocker) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    mocker.patch("asyncio.Semaphore.locked", return_value=False)
    args = argparse.Namespace(
        verbose=False,
        log=resp_string_io,
        last_id=1,
        requests=10,
        output=StringIO("")
    )
    with does_not_raise():
        cmain.crawl(args)


def test_parse_main() -> None:
    args = argparse.Namespace(
        verbose=False, input=resp_string_io, output=StringIO("")
    )
    with does_not_raise():
        pmain.parse(args)

