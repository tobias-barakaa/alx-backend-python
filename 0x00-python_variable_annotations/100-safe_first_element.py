#!/usr/bin/env python3
"""
Basic annotations - safe_first_element
"""
from typing import Union, Any, List


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Augment the following code with
    the correct duck-typed annotations:
    """
    if lst:
        return lst[0]
    else:
        return None
