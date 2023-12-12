#!/usr/bin/env python3
"""
coroutine function that take no argument
"""
import random
import asyncio


async def async_generator():
    """
    coroutine that yields random number
    between 1 to 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 9)
