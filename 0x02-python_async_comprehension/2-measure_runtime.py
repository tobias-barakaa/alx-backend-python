#!/usr/bin/env python3

"""
coroutine function that take no argument
"""
import asyncio
from typing import List
import time
from random import uniform
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime and return it.
    """
    start = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_running_loop().time()
    return end
