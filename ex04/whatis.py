
"""
whatis.py — Determine if a single integer argument is odd or even.

Behavior:
- No output if no argument is provided.
- Prints "I'm Even." or "I'm Odd." for a single integer argument.
- Prints an AssertionError message for invalid input or too many arguments.
"""

# Import sys module to access command-line arguments.
import sys


def parity_message(n: int) -> str:
    """Return the parity message for integer n.

    Parameters:
        n: The integer to check.

    Returns:
        "I'm Even." if n is even, otherwise "I'm Odd."
    """
    return "I'm Even." if n % 2 == 0 else "I'm Odd."


def main() -> None:
    argv = sys.argv
    argc = len(argv)

    if argc == 1:
        return

    if argc > 2:
        print("AssertionError: more than one argument is provided")
        return

    candidate = argv[1]
    try:
        value = int(candidate)
    except (ValueError, TypeError):
        print("AssertionError: argument is not an integer")
        return

    print(parity_message(value))


if __name__ == "__main__":
    main()

# USAGE:
# python3 whatis.py  # No output
# python3 whatis.py 42  # Outputs: I'm Even.
# python3 whatis.py 7  # Outputs: I'm Odd.