#!/usr/bin/env python3
"""
Basic annotations - to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as
    arguments and returns a tuple.
    """
    return (k, v**2)
