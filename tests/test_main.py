"""Tests of the cmed command-line interface entry point."""

# Standard library imports
import argparse
from contextlib import nullcontext as does_not_raise
import sys

# Local library imports
from med_crawler import __main__
from .resp import MockResp


def test_main(mocker) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    mocker.patch("asyncio.Semaphore.locked", return_value=False)
    args = argparse.Namespace(verbose=False, last_id=100, output=sys.stderr)
    with does_not_raise():
        __main__.parse(args)
