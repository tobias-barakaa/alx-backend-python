#!/usr/bin/env python3
"""
function that takes a list input_list of
floats as argument and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of floats and integers and
    returns their sum as a float.
    """
    return sum(mxd_lst)
