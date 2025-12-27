from __future__ import annotations

import pytest

import pythonbible as bible


def test_count_books_single_book() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references("James 1:4-6")

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(references[0])  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_books == 1


def test_count_books_two_books() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Matthew 19:3 - Mark 6:9",
    )

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(references[0])  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_books == 2


def test_count_books_multiple_books() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Genesis - Deuteronomy",
    )

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(references[0])  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_books == 5


def test_count_books_multiple_references() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Genesis - Deuteronomy, Matthew 19:3 - Mark 6:9, James 1:4-6",
    )

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(references)

    # Then the count is correct
    assert number_of_books == 5 + 2 + 1


def test_count_books_string() -> None:
    # Given a string containing one or more Scripture references
    reference: str = "Genesis - Deuteronomy, Matthew 19:3 - Mark 6:9, James 1:4-6"

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(reference)  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_books == 5 + 2 + 1


def test_count_chapters_single_chapter() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references("James 1:4-6")

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(
        references[0],  # type: ignore[arg-type]
    )

    # Then the count is correct
    assert number_of_chapters == 1


def test_count_chapters_two_chapters() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references("James 1-2")

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(
        references[0],  # type: ignore[arg-type]
    )

    # Then the count is correct
    assert number_of_chapters == 2


def test_count_chapters_multiple_chapters() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references("James")

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(
        references[0],  # type: ignore[arg-type]
    )

    # Then the count is correct
    assert number_of_chapters == 5


def test_count_chapters_multiple_books() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Matthew 28:1 - Luke 1:10",
    )

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(
        references[0],  # type: ignore[arg-type]
    )

    # Then the count is correct
    assert number_of_chapters == 1 + 16 + 1


def test_count_chapters_multiple_references() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Genesis, Matthew - Acts",
    )

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(references)

    # Then the count is correct
    assert number_of_chapters == 50 + 28 + 16 + 24 + 21 + 28  # 167 total


def test_count_chapters_string() -> None:
    # Given a string containing one or more Scripture references
    reference: str = "Genesis, Matthew - Acts"

    # When we get the count of chapters in the reference
    number_of_chapters: int = bible.count_chapters(reference)  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_chapters == 50 + 28 + 16 + 24 + 21 + 28  # 167 total


def test_count_verses_single_verse() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references("Genesis 1:1")

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references[0])  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_verses == 1


def test_count_verses_multiple_verses() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references("Genesis 1:6-10")

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references[0])  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_verses == 5


def test_count_verses_multiple_chapters() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Matthew 5:3-7:27",
    )

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references[0])  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_verses == 46 + 34 + 27


def test_count_verses_multiple_books() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references("1 John - Jude")

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references[0])  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_verses == (10 + 29 + 24 + 21 + 21) + 13 + 14 + 25


def test_count_verses_multiple_references() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Genesis 1:1; John 3:16; Romans 15:5-7,13",
    )

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references)

    # Then the count is correct
    assert number_of_verses == 1 + 1 + (3 + 1)


def test_count_verses_string() -> None:
    # Given a string containing one or more Scripture references
    reference: str = "Genesis 1:1; John 3:16; Romans 15:5-7,13"

    # When we get the count of verses in the reference
    number_of_verses: int = bible.count_verses(reference)  # type: ignore[arg-type]

    # Then the count is correct
    assert number_of_verses == 1 + 1 + (3 + 1)


def test_count_verses_in_old_testament() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Genesis - Malachi"
    )

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references)

    # Then the count is correct
    assert number_of_verses == 23145


def test_count_verses_in_new_testament() -> None:
    # Given a list of references
    references: list[bible.NormalizedReference] = bible.get_references(
        "Matthew - Revelation"
    )

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references)

    # Then the count is correct
    assert number_of_verses == 7957


@pytest.mark.parametrize(
    ("reference_text", "expected_verses"),
    [
        ("Genesis 31", 55),
        ("Genesis 32", 32),
        ("Exodus 7", 25),
        ("Exodus 8", 32),
        ("Exodus 21", 36),
        ("Exodus 22", 31),
        ("Leviticus 5", 19),
        ("Leviticus 6", 30),
        ("Numbers 16", 50),
        ("Numbers 17", 13),
        ("Numbers 29", 40),
        ("Numbers 30", 16),
        ("Deuteronomy 12", 32),
        ("Deuteronomy 13", 18),
        ("Deuteronomy 22", 30),
        ("Deuteronomy 23", 25),
        ("Deuteronomy 28", 68),
        ("Deuteronomy 29", 29),
        ("1 Samuel 21", 15),
        ("1 Samuel 23", 29),
        ("1 Samuel 24", 22),
        ("1 Samuel 25", 44),
        ("2 Samuel 18", 33),
        ("2 Samuel 19", 43),
        ("2 Kings 11", 21),
        ("2 Kings 12", 21),
        ("Ecclesiastes 4", 16),
        ("Ecclesiastes 5", 20),
        ("Song of Songs 6", 13),
        ("Song of Songs 7", 13),
        ("Jeremiah 8", 22),
        ("Jeremiah 9", 26),
        ("Ezekiel 20", 49),
        ("Ezekiel 21", 32),
        ("Hosea 1", 11),
        ("Hosea 2", 23),
        ("Hosea 11", 12),
        ("Hosea 12", 14),
        ("Hosea 13", 16),
        ("Hosea 14", 9),
        ("Jonah 1", 17),
        ("Jonah 2", 10),
        ("Micah 4", 13),
        ("Micah 5", 15),
        ("Nahum 1", 15),
        ("Nahum 2", 13),
        ("Zechariah 1", 21),
        ("Zechariah 2", 13),
        ("Malachi 3", 18),
        ("Malachi 4", 6),
    ],
)
def test_verses_in_select_chapters(reference_text: str, expected_verses: int) -> None:
    """Test that select chapters have the correct number of verses based
    on the KJV. The verses counts are manual corrections from the following
    source.
    """
    # https://www.life-everlasting.net/pages/bible/Number%20of%20verses%20per%20chapter%20in%20Bible%20(KJV).pdf
    reference: bible.NormalizedReference = bible.get_references(reference_text)[0]
    assert bible.count_verses([reference]) == expected_verses
