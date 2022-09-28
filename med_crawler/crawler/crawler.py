"""Middle English Dictionary crawler code."""

# Standard library imports
from __future__ import annotations
import asyncio
from dataclasses import dataclass
import requests
from typing import Any, ClassVar, Coroutine
import urllib.parse

# Third-party library imports
from tqdm import tqdm


__all__ = ["Crawler", "WebContents", "LAST_MED_ENTRY_ID"]


LAST_MED_ENTRY_ID = 54_083


@dataclass(slots=True, frozen=True)
class WebContents:
    text: str
    status_code: int

    @property
    def ok(self) -> bool:
        return self.status_code == 200


class Crawler:
    url: ClassVar[str] = (
        "https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary/"
    )

    def __init__(
        self,
        last_entry_id: int = LAST_MED_ENTRY_ID,
        concurrent_requests: int = 10,
    ) -> None:
        self.last_entry_id = last_entry_id
        self.semaphore = asyncio.Semaphore(concurrent_requests)

    def crawl(self, verbose: bool = False) -> list[WebContents]:
        result = asyncio.run(self.crawl_asyc(verbose))
        return result

    async def crawl_asyc(self, verbose: bool = False) -> list[WebContents]:
        result: list[WebContents] = []
        tasks: list[Coroutine[Any, Any, WebContents]] = []

        if verbose:
            bar = tqdm(total=self.last_entry_id, desc="crawling MED:")
        else:
            bar = None

        for id in range(1, self.last_entry_id+1):
            tasks.append(self.http_get(id, bar=bar))
        result.extend(await asyncio.gather(*tasks))
        return result

    async def http_get(
        self, id: int = 0, **kwargs: tqdm | None
    ) -> WebContents:
        async with self.semaphore:
            result = await asyncio.to_thread(self.http_get_sync, id)
            if self.semaphore.locked():
                await asyncio.sleep(1)
            if result.ok:
                if b := kwargs.get("bar", None):
                    b.update(1)
                return result
        raise ValueError(f"Unexpected status code: {result.status_code}")

    def http_get_sync(self, id: int = 0) -> WebContents:
        url = urllib.parse.urljoin(self.url, f"MED{id}")
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            return WebContents("", response.status_code)
        else:
            return WebContents(response.text, response.status_code)
