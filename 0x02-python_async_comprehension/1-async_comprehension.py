#!/usr/bin/env python3

"""
coroutine function that take no argument
"""
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """
    coroutine that collect 10 random numbers
    between 0 and 10
    """
    return [random.uniform(0, 10) for _ in range(10)]
