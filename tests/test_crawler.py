"""Tests of the Middle English Dictionary crawler."""

# Standard library imports
import asyncio
from dataclasses import dataclass

# Third-party library imports
import pytest

# Local library imports
from med_crawler.crawler import crawler


WEB_CONTENTS = "Hello, world!"


@dataclass
class MockResp:
    text: str = WEB_CONTENTS

    def raise_for_status(self) -> None:
        return None

    @property
    def status_code(self) -> int:
        return 200


@pytest.mark.parametrize("id", [1, 10_000, 0, 14, 5])
def test_crawler_http_get_sync(mocker, id: int) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    c = crawler.Crawler()
    result = c.http_get_sync(id)
    assert result.text == WEB_CONTENTS
    assert result.status_code == 200


@pytest.mark.parametrize("id", [1, 10_000, 0, 14, 5])
def test_crawler_http_get_async(mocker, id: int) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    c = crawler.Crawler()
    result = asyncio.run(c.http_get(id))
    assert result.text == WEB_CONTENTS
    assert result.status_code == 200


def test_crawler_public_sync_crawl(mocker) -> None:
    mocker.patch("requests.get", return_value=MockResp())
    c = crawler.Crawler(100)
    result = c.crawl()
    assert len(result) == 99
