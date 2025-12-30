"""
Loading.py — Simple progress bar generator (ft_tqdm).

Behavior:
    - ft_tqdm takes a range (or any iterable with a known length)
      and yields its elements, just like the built-in tqdm iterator.

    - On each iteration, it prints a progress bar on a single line,
      updated in place, in the form:

        100%|[==============================]| 333/333

"""

# Iterable, Iterator are protocol types used only for type hints:
# - Iterable[T]: something you can loop over
# - Iterator[T]: something that yields items one by one
from collections.abc import Iterable, Iterator

# TypeVar lets us define a generic type T so ft_tqdm can work with any type
# (ints, strings, custom objects, etc.) without changing the code.
from typing import TypeVar

T = TypeVar("T")


def ft_tqdm(lst: Iterable[T]) -> Iterator[T]:
    """A minimal tqdm-like progress bar using a generator.

    Parameters:
        lst:
            Any iterable with a known length.

    Yields:
        Each element of lst, one by one, while updating a progress bar.
    """
    items = list(lst)
    total = len(items)
    if total == 0:
        return

    bar_length = 50

    for idx, elem in enumerate(items, start=1):
        progress = idx / total
        percent = int(progress * 100)

        filled_length = int(bar_length * progress)
        # The bar uses '=' for completed part and spaces for the rest.
        bar = "=" * filled_length + " " * (bar_length - filled_length)

        # '\r' returns carriage to the start of the line,
        # end='' avoids printing a newline, flush ensures immediate update.
        print(f"\r{percent:3d}%|[{bar}]| {idx}/{total}", end="", flush=True)

        # 'yield' turns this function into a generator:
        # - It produces one value at a time.
        # - Execution pauses at 'yield elem' and resumes on the next iteration.
        # - This makes ft_tqdm behave like an iterator, just like tqdm:
        #       it updates the progress bar, then hands back the next element.
        yield elem

    # Finish with a newline so the next print starts on a new line.
    print()


if __name__ == "__main__":
    pass

# USAGE:
# python3 tester.py
