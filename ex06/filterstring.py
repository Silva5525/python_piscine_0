"""
filterstring.py — Filter words in a string by length.

Behavior:
    The program accepts exactly two arguments:
        1) A string S
        2) An integer N

    It prints a Python list of the words from S whose length is strictly
    greater than N.

    - Words are separated by spaces.
    - Strings do not contain special characters.
    - The program must use:
        - at least one list comprehension
        - at least one lambda

"""

import sys
from ft_filter import ft_filter


def parse_args(argv: list[str]) -> tuple[str, int] | None:
    """Validate and parse command-line arguments.

    Returns:
        (text, n) if arguments are valid, otherwise None (and prints error).
    """
    if len(argv) != 3:
        print("AssertionError: the arguments are bad")
        return None

    text = argv[1]
    n_str = argv[2]

    if text.isdigit():
        print("AssertionError: the arguments are bad")
        return None

    try:
        n = int(n_str)
    except (ValueError, TypeError):
        print("AssertionError: the arguments are bad")
        return None

    return text, n


def filter_words_longer_than(text: str, n: int) -> list[str]:
    """Return a list of words from text whose length is > n.

    Uses:
        - a list comprehension to split text into words
        - a lambda with ft_filter to select the words
    """
    # List comprehension: build a list of words from the string.
    words = [word for word in text.split()]

    # Lambda: predicate for ft_filter.
    predicate = lambda w: len(w) > n  # noqa: E731 (new line explanation)
    # noqua (would ignore all warnings for that line.)
    # noqa: E731 (Ignores only warning E731 on this line.)

    return list(ft_filter(predicate, words))


def main() -> None:
    parsed = parse_args(sys.argv)
    if parsed is None:
        return

    text, n = parsed
    result = filter_words_longer_than(text, n)
    print(result)


if __name__ == "__main__":
    main()

# USAGE:
# python3 filterstring.py "Hello the World" 4
