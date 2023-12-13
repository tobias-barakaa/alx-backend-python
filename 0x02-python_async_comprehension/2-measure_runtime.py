#!/usr/bin/env python3

"""
coroutine function that takes no argument
"""
import asyncio
import time
from random import uniform
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of a coroutine.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()

    await asyncio.gather(async_comprehension() for _ in range(4))
    end_time = time.time()
    return end_time - start_time

