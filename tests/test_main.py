"""Tests of the cmed CLI entry point."""

# Standard library imports
from contextlib import nullcontext as does_not_raise

# Local library imports
from med_crawler import __main__


def test_main() -> None:
    with does_not_raise():
        __main__.main()
