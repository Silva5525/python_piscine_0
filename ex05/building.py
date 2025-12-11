"""
building.py — Count character categories in a given text.

Behavior:
- If no argument is provided:
    • Prompt the user: "What is the text to count?"
    • Read from standard input until EOF (so the final newline is included).
- If exactly one argument is provided:
    • Use that argument as the text to analyze.
- If more than one argument is provided:
    • Print "AssertionError: more than one argument is provided".

The program displays:
- Total number of characters
- Number of upper-case letters
- Number of lower-case letters
- Number of punctuation marks
- Number of spaces (any whitespace, including newlines)
- Number of digits
"""

import sys


def count_text_stats(text: str) -> dict:
    """Return statistics about the characters in the given text.

    The returned dictionary contains:
        - "upper": number of upper-case letters
        - "lower": number of lower-case letters
        - "punct": number of punctuation marks
        - "spaces": number of whitespace characters
        - "digits": number of digits
        - "length": total number of characters
    """
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    digits = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            punct += 1

    return {
        "upper": upper,
        "lower": lower,
        "punct": punct,
        "spaces": spaces,
        "digits": digits,
        "length": len(text),
    }


def print_stats(stats: dict) -> None:
    print(f"The text contains {stats['length']} characters:")
    print(f"{stats['upper']} upper letters")
    print(f"{stats['lower']} lower letters")
    print(f"{stats['punct']} punctuation marks")
    print(f"{stats['spaces']} spaces")
    print(f"{stats['digits']} digits")


def main() -> None:
    argv = sys.argv
    argc = len(argv)

    if argc > 2:
        print("AssertionError: more than one argument is provided")
        return

    if argc == 2:
        text = argv[1]
    else:
        # No argument: prompt the user and read from stdin until EOF.
        # The newline (carriage return) will be part of the text and
        # thus counted as a space via str.isspace().
        print("What is the text to count?")
        try:
            text = sys.stdin.read()
        except Exception:
            return

    stats = count_text_stats(text)
    print_stats(stats)


if __name__ == "__main__":
    main()

# USAGE:
#   python3 building.py \
#       "Python 3.0, released in 2008."
#   [Ctrl + D]
