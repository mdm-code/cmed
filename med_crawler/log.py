"""Logging components."""

# Standard library imports
import enum
from typing import Generator, TextIO, Protocol


class LoggingError(Exception):
    ...


class Level(str, enum.Enum):
    ok = OK = "OK"
    warning = WARN = "WARNING"
    error = ERROR = "ERROR"


class Logger(Protocol):
    def __init__(self, out: TextIO) -> None:
        raise NotImplementedError

    def log(self, msg: str, lvl: Level) -> None:
        raise NotImplementedError


class CrawlerLogger:
    def __init__(self, out: TextIO) -> None:
        self.out = out
        self.counter = count(0, 1)

    def log(self, msg: str, lvl: Level) -> None:
        match lvl:
            case lvl.ok | lvl.error | lvl.warning:
                self.out.write(f"{next(self.counter)} {format(lvl)}: {msg}\n")
                self.out.flush()
            case _:
                raise LoggingError(f"{str(lvl)} not supported")


def count(start: int = 0, step: int = 1) -> Generator[int, None, None]:
    while True:
        yield start
        start += step
