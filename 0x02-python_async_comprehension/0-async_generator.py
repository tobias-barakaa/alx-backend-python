#!/usr/bin/env python3
"""
coroutine function that takes no argument
"""
import asyncio
import random


async def async_generator():
    """
    coroutine that yields random numbers
    between 1 to 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
