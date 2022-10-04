"""Tests of the logging component."""


from med_crawler import log
import sys
import contextlib
from io import StringIO


def test_crawler_logger() -> None:
    out = StringIO()
    with contextlib.redirect_stdout(out):
        l = log.CrawlerLogger(sys.stdout, False)
        l.log("this is a warning", log.Level.WARN)
        l.log("this is an error!", log.Level.ERROR)
    out.seek(0)
    assert out.readlines() == [
        "0::WARNING::this is a warning\n",
        "1::ERROR::this is an error!\n",
    ]

