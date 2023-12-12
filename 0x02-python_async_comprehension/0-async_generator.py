#!/usr/bin/env python3
"""
coroutine function that takes no argument
"""
import random
import asyncio


async def async_generator():
    """
    coroutine that yields random numbers
    between 1 to 10
    """
    async def generate_random():
        await asyncio.sleep(1)
        return random.uniform(0, 10)

    return [await generate_random() for _ in range(10)]
