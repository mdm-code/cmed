"""Tests of the Middle English Dictionary crawler."""

# Standard library imports
import asyncio

# Third-party library imports
import pytest

# Local library imports
from med_crawler import crawler
from .resp import MockResp, resp_text


@pytest.mark.parametrize("id", [1, 10_000, 0, 14, 5])
def test_crawler_http_get_sync(mocker, id: int) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    mocker.patch("asyncio.Semaphore.locked", return_value=False)
    c = crawler.Crawler()
    result = c.http_get_sync(id)
    assert result.text == resp_text
    assert result.status_code == 200


@pytest.mark.parametrize("id", [1, 10_000, 0, 14, 5])
def test_crawler_http_get_async(mocker, id: int) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    mocker.patch("asyncio.Semaphore.locked", return_value=False)
    c = crawler.Crawler()
    result = asyncio.run(c.http_get(id))
    assert result.text == resp_text
    assert result.status_code == 200


def test_crawler_public_sync_crawl(mocker) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    mocker.patch("asyncio.Semaphore.locked", return_value=False)
    c = crawler.Crawler(3)
    result = c.crawl()
    assert len(result) == 2
