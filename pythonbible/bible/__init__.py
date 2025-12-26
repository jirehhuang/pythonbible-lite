from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import TYPE_CHECKING

from pythonbible.bible.bible import Bible
from pythonbible.books import Book
from pythonbible.versions import Version

if TYPE_CHECKING:
    from pythonbible.bible.bible import Bible
    from pythonbible.versions import Version


CURRENT_FOLDER = Path(__file__).parent

BIBLES: dict[Version, dict[str, Bible]] = {}


def get_bible(version: Version, bible_type: str) -> Bible:
    """Return the Bible for the given version and format.

    :param version: The version of the Bible
    :type version: Version
    :param bible_type: The type of the Bible
    :type bible_type: str
    :return: The Bible for the given version and type
    :rtype: Bible
    """
    return Bible(
        version=Version.AMERICAN_STANDARD,
        scripture_content="",
        verse_start_indices={0: 0},
        verse_end_indices={0: 0},
        max_verses={Book.GENESIS: {0: 0}},
        short_titles={},
        long_titles={},
        is_html=False,
    )


def add_bible(version: Version, bible_type: str, version_bible: Bible) -> None:
    """Add the Bible to the dictionary of Bibles.

    This should allow a user to BYOB (bring your own Bible) to the library, which can
    be useful if a user has licensed a copyrighted Bible (which is not included in the
    pythonbible library) for use within their application.

    :param version: The version of the Bible
    :type version: Version
    :param bible_type: The type of the Bible
    :type bible_type: str
    :param version_bible: The Bible to add
    :type version_bible: Bible
    """
    return


def _do_version_files_exist(version: Version) -> bool:
    return False
