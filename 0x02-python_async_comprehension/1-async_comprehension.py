#!/usr/bin/env python3

"""
coroutine function that take no argument
"""
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        list: A list of 10 random numbers.
    """
    async for _ in async_generator():
        yield random.randint(1, 9)
