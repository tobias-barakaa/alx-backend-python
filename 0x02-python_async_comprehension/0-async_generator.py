#!/usr/bin/env python3
"""
coroutine function that takes no arguments
"""
import asyncio
import random

async def async_generator() -> float:
    """
    Asynchronous generator that yields random numbers
    between 0 and 10 after waiting for 1 second.

    Yields:
        float: A random float value between 0 and 10.
    """
    while count < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        count += 1
