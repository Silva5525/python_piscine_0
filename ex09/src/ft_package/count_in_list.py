"""
# ft_package — A sample test package.

count_in_list: return the number of occurrences of an element in a list.
"""

from typing import Any, List


def count_in_list(items: List[Any], target: Any) -> int:
    """
    Count the number of times `target` appears in `items`.

    Parameters
    ----------
    items : list
        List to search.
    target : Any
        Element to count.

    Returns
    -------
    int
        Number of occurrences.
    """
    return sum(1 for x in items if x == target)


# from collections.abc import Iterable
# from typing import Any


# def count_in_list(iterable: Iterable[Any], item: Any) -> int:
#     """Count how many times `item` appears in `iterable`.

#     Parameters:
#         iterable:
#             Any iterable of elements (list, tuple, generator, etc.).
#         item:
#             The value to count inside the iterable.

#     Returns:
#         int: The number of occurrences of `item` in `iterable`.
#     """
#     # We avoid using list.count so that this works with *any* iterable,
#     # not just lists.
#     return sum(1 for element in iterable if element == item)


__all__ = ["count_in_list"]
