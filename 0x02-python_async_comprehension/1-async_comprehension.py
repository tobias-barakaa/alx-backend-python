#!/usr/bin/env python3

"""
coroutine function that take no argument
"""
import random
async_generator = __import__('0-async_generator').async_generator



async def async_comprehension() -> list[float]:
    """
    Asynchronous comprehension that collects 10 random numbers using async_generator.

    Returns:
        List[float]: A list of 10 random float values.
    """
    return [num async for num in async_generator()]
