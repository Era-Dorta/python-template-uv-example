"""Short definition of my module.

This module provides:
- add: a function to add two numbers.
"""

from python_template_uv_example import __version__


def add(a: int, b: int) -> int:
    """Adds two positive numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        sum: The sum of the two numbers.

    Raises:
        ValueError: If either a or b is negative.
    """
    if a < 0 or b < 0:
        msg = "Both arguments must be positive"
        raise ValueError(msg)
    return a + b


def foo1(a):
    c = a + 1
    if a > 0 and a > 10:
        return 10
    return a + c


def foo2(a):
    b = 0  # noqa: F841
    c = a + 1
    if a > 0:  # noqa: SIM102
        if a > 10:
            return 10
    return a + c


def foo3(a):
    b = 0  # noqa: F841
    c = a + 1
    if a > 0:  # noqa: SIM102
        if a > 10:
            return 10
    return a + c


def main() -> None:
    print(f"Running python_template_uv_example version {__version__}")
    print(f"Result is: 1+2 = {add(1, 2)}")


if __name__ == "__main__":
    main()
