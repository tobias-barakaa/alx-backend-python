#!/usr/bin/env python3
"""
Zoom Array - Zoom in on elements of a tuple.

Parameters:
    lst (Tuple): The tuple to zoom in on.
    factor (int, optional): The zoom factor, defaults to 2.

Returns:
    List: The zoomed-in list of elements.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
