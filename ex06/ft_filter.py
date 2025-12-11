"""
ft_filter.py — Reimplementation of the built-in filter function.

This module defines ft_filter, which behaves like Python's built-in filter:

    ft_filter(function or None, iterable) -> iterator

- If function is None, it returns all elements of the iterable that are truthy.
- Otherwise, it returns all elements for which function(element) is true.
"""

# Callable and Iterable are imported from collections.abc:
# - Callable[[T], bool] takes one argument of type T and returns a bool.
# - Iterable[T] object you can loop over (lists, tuples, ranges, etc.).
from collections.abc import Callable, Iterable

# TypeVar, Iterator, and Optional for generic, well-documented types:
# - TypeVar("T") writes ft_filter in a generic way,
# works with any element type.
# - Iterator[T] describes the return type:
# an object you can iterate over, yielding elements of type T.
# - Optional[Callable[[T], bool]]
# means the function argument can be either a Callable or None.
from typing import TypeVar, Iterator, Optional

T = TypeVar("T")


def ft_filter(function: Optional[Callable[[T], bool]],
              iterable: Iterable[T]) -> Iterator[T]:
    """Return an iterator yielding items from iterable
     for which function(item) is true.

    Parameters:
        function:
            A function taking one argument and returning True or False.
            If None, the identity of bool() is used.
        iterable:
            Any iterable providing the items to filter.

    Returns:
        An iterator over the filtered elements.
    """
    # If function is None, use bool as the predicate, like the built-in filter.
    predicate: Callable[[T], bool]
    if function is None:
        predicate = bool
    else:
        predicate = function

    return (item for item in iterable if predicate(item))


if __name__ == "__main__":
    pass

# USAGE:
# python3 filterstring.py "Hello the World" 4
