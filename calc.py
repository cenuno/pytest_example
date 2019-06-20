from typing import List, Tuple


def calc_min_max(x: List[int]) -> Tuple[int, int]:
    """
    Calculates the minimum and maximum values of a list of integers

    Returns:
    -------
    Tuple with the first value being the min and the second value being the max
    """
    # sort vector in ascending order
    x.sort()
    return (x[0], x[-1])
