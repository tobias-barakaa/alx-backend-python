#!/usr/bin/env python3
"""
coroutine function that takes no arguments
"""
import asyncio
import random

async def async_generator() -> float:
    """
    Coroutine that yields random numbers between 0 and 10 after waiting for 1 second.

    Returns:
        float: A random float value between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

