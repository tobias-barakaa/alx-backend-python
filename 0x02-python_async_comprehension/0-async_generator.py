#!/usr/bin/env python3
"""
coroutine function that takes no arguments
"""
import asyncio
import random

async def async_generator() -> float:
    """
    Coroutine that generates a list of random numbers between 0 and 10 after waiting for 1 second.

    Returns:
        List[float]: A list of random float values between 0 and 10.
    """
    result = []
    for _ in range(10):
        await asyncio.sleep(1)
        result.append(random.uniform(0, 10))
    return result
