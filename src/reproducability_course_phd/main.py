"""Short definition of my module."""

from reproducability_course_phd import __version__


def add(a: int, b: int) -> int:
    """Adds two positive numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.

    Raises:
        ValueError: If either a or b is negative.
    """
    if a < 0 or b < 0:
        msg = "Both arguments must be positive"
        raise ValueError(msg)
    return a + b


def foo1(a):
    b = 0
    c = a + 1
    if a > 0 and a > 10:
        return 10
    return a + b + c


def main() -> None:
    print(f"Running reproducability_course_phd version {__version__}")
    print(f"Result is: 1+2 = {add(1, 2)}")


if __name__ == "__main__":
    main()
