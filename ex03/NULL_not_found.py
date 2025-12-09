
def NULL_not_found(object: any) -> int:
    """
    Print the 'null-like' type category of the given object.
    Returns 0 for recognized categories, 1 otherwise.

    Categories:
      - Nothing: None
      - Cheese: float('nan')
      - Zero: 0 (int)
      - Empty: '' (str)
      - Fake: False (bool)
    """
    # None
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0

    # NaN (must check via self-inequality)
    if isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0

    # Bool before int (since bool is a subclass of int)
    if isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0

    # Zero (int)
    if isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0

    # Empty string
    if isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0

    # Not found
    print("Type not Found")
    return 1


if __name__ == "__main__":
    # Running this file directly should do nothing.
    pass

# python3 tester.py | cat -e
