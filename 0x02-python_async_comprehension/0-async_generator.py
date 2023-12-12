#!/usr/bin/env python3
"""
coroutine function that takes no arguments
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields
    random numbers between 0 and 10 after waiting for 1 second.

    Yields:
        float: A random float value between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
