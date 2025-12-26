"""Contains the Bible class."""

from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING

from pythonbible.bible.errors import VersionMissingVerseError
from pythonbible.errors import InvalidVerseError
from pythonbible.validator import is_valid_verse_id

if TYPE_CHECKING:
    from pythonbible.books import Book
    from pythonbible.versions import Version


class Bible:
    """The Bible class.

    The Bible class contains the scripture content for a version and format along with
    the functionality necessary to get the scripture content for a verse or range of
    verses.
    """

    version: Version
    scripture_content: str
    verse_start_indices: dict[int, int]
    verse_end_indices: dict[int, int]
    max_verses: dict[Book, dict[int, int]]
    short_titles: dict[Book, str]
    long_titles: dict[Book, str]
    is_html: bool

    def __init__(
        self: Bible,
        version: Version,
        scripture_content: str,
        verse_start_indices: dict[int, int],
        verse_end_indices: dict[int, int],
        max_verses: dict[Book, dict[int, int]],
        short_titles: dict[Book, str],
        long_titles: dict[Book, str],
        is_html: bool = False,
    ) -> None:
        """Initialize a Bible object.

        :param version: The version of the Bible.
        :param scripture_content: The scripture content for the Bible.
        :param verse_start_indices: The start indices for each verse.
        :param verse_end_indices: The end indices for each verse.
        :param max_verses: The maximum verses for each book and chapter.
        :param short_titles: The short titles for each book.
        :param long_titles: The long titles for each book.
        :param is_html: Whether the scripture content is HTML.
        """
        self.version = version
        self.scripture_content = scripture_content
        self.verse_start_indices = verse_start_indices
        self.verse_end_indices = verse_end_indices
        self.max_verses = max_verses
        self.short_titles = short_titles
        self.long_titles = long_titles
        self.is_html = is_html

    def get_scripture(
        self: Bible,
        start_verse_id: int,
        end_verse_id: int | None = None,
    ) -> str:
        return ""

    def _get_start_and_end_indices(
        self: Bible,
        start_verse_id: int,
        end_verse_id: int,
    ) -> tuple[int, int]:
        return 0, 0


@lru_cache()
def _clean(scripture_content: str, is_html: bool) -> str:
    return ""


@lru_cache()
def clean_html(scripture_content: str) -> str:
    return ""
