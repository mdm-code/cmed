"""Tests of the Middle English Dictionary crawler."""

# Standard library imports
from io import StringIO

# Third-party library imports
import pytest

# Local library imports
from med_crawler import crawler
from med_crawler import log
from .resp import MockResp, resp_text


@pytest.fixture(scope="function")
def mock_io() -> StringIO:
    return StringIO("")


@pytest.mark.parametrize("id", [1, 10_000, 0, 14, 5])
def test_crawler_http_get_sync(mocker, id: int, mock_io) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    mocker.patch("asyncio.Semaphore.locked", return_value=False)
    c = crawler.Crawler(mock_io, log.CrawlerLogger(mock_io))
    result = c.http_get_sync(id)
    assert result.text == resp_text
    assert result.status_code == 200


def test_crawler_public_sync_crawl(mocker, mock_io) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    mocker.patch("asyncio.Semaphore.locked", return_value=False)
    c = crawler.Crawler(mock_io, log.CrawlerLogger(mock_io), 3)
    result = c.crawl(False)
    assert len(result) == 3
