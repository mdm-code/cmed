"""Middle English Dictionary crawler code."""

# Standard library imports
from __future__ import annotations
import asyncio
from dataclasses import dataclass
import requests
from typing import Any, ClassVar, Coroutine
import urllib.parse


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
        last_id: int = LAST_MED_ENTRY_ID,
        simultaneous_requests: int = 30,
    ) -> None:
        self.last_id = last_id
        self.sem = asyncio.Semaphore(simultaneous_requests)

    def crawl(self) -> list[WebContents]:
        result = asyncio.run(self.crawl_asyc())
        return result

    async def crawl_asyc(self) -> list[WebContents]:
        result: list[WebContents] = []
        tasks: list[Coroutine[Any, Any, WebContents]] = []
        for id in range(1, self.last_id):
            tasks.append(self.http_get(id))
        result.extend(await asyncio.gather(*tasks))
        return result

    async def http_get(self, id: int = 0) -> WebContents:
        async with self.sem:
            return await asyncio.to_thread(self.http_get_sync, id)

    def http_get_sync(self, id: int = 0) -> WebContents:
        url = urllib.parse.urljoin(self.url, f"MED{id}")
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            return WebContents("", response.status_code)
        else:
            return WebContents(response.text, response.status_code)
