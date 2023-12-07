#!/usr/bin/env python3
"""
basic annotation - element_length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences (lst) as an argument
    and returns a list of tuples, each containing a sequence
    from the input and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
