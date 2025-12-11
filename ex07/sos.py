"""
sos.py — Encode a given string into Morse code.

Behavior:
    - The program takes exactly ONE argument: a string to encode.
    - It supports:
        - letters A-Z (case-insensitive)
        - digits 0-9
        - space characters

    - Output:
        - Each Morse character is separated by a single space.
        - A space in the input is encoded as '/'.

    - If the number of arguments is not 1, or if the string contains
      unsupported characters (anything other than alphanumeric or spaces),
      it prints:

        "AssertionError: the arguments are bad"
"""

import sys

NESTED_MORSE: dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}


def encode_morse(text: str) -> str:
    """Encode the given text string into Morse code.

    The function:
        - Converts text to uppercase.
        - Validates that all characters are alphanumeric or spaces.
        - Uses NESTED_MORSE to map each character to Morse.

    Parameters:
        text: The input string to encode.

    Returns:
        A string with Morse code, where each encoded unit is separated
        by a single space.

    Raises:
        ValueError: If text contains unsupported characters.
    """
    morse_parts: list[str] = []
    for ch in text.upper():
        if ch not in NESTED_MORSE:
            raise ValueError(f"Unsupported character: {ch!r}")
        morse_parts.append(NESTED_MORSE[ch])
    return " ".join(morse_parts)


def main() -> None:
    """Main entry point for the script.

    Validates command-line arguments and prints either:
        - The Morse-encoded string
        - Or an AssertionError message if the arguments are invalid.
    """
    argv = sys.argv
    if len(argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    text = argv[1]

    try:
        encoded = encode_morse(text)
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    print(encoded)


if __name__ == "__main__":
    main()

# USAGE:
# python3 sos.py "Hello 42" | cat -e
