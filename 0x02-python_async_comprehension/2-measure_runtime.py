#!/usr/bin/env python3

"""
coroutine function that take no argument
"""
import asyncio
from typing import List
import time
from random import uniform
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Measures the runtime of a coroutine.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(async_comprehension() for _ in range(4))

    end_time = time.perf_counter()
    return end_time - start_time
