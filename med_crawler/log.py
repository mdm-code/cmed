"""Logging components."""

# Standard library imports
import datetime
import enum
from typing import Generator, TextIO, Protocol, ClassVar


class LoggingError(Exception):
    ...


class Level(str, enum.Enum):
    ok = OK = "OK"
    warning = WARN = "WARNING"
    error = ERROR = "ERROR"


class Logger(Protocol):
    def log(self, msg: str, lvl: Level) -> None:
        raise NotImplementedError


class CrawlerLogger:
    date_fmt: ClassVar[str] = "%y-%m-%d %H:%M:%S.%f"

    def __init__(self, out: TextIO, include_date: bool = True) -> None:
        self.out = out
        self.include_date = include_date
        self.counter = count(0, 1)

    def log(self, msg: str, lvl: Level) -> None:
        match lvl:
            case lvl.ok | lvl.error | lvl.warning:
                if self.include_date:
                    time = datetime.datetime.now().strftime(self.date_fmt)
                    self.out.write(
                        f"{next(self.counter)}::{format(lvl)}::{time}::{msg}\n"
                    )
                else:
                    self.out.write(
                        f"{next(self.counter)}::{format(lvl)}::{msg}\n"
                    )
                self.out.flush()
            case _:
                raise LoggingError(f"{str(lvl)} not supported")


def count(start: int = 0, step: int = 1) -> Generator[int, None, None]:
    while True:
        yield start
        start += step
