#!/usr/bin/env python3
from typing import List

"""define and annotate the following variables with the specified values:"""


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats (input_list) as an
    argument
    and returns their sum as a float.
    """
    if not all(isinstance(x, float) for x in input_list):
        raise TypeError("All elements in the list must be floats.")
    return sum(input_list)
