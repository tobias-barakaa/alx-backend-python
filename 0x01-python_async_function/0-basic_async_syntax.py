#!/usr/bin/env python3
"""
Python function to print
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    funtion that return
    random value(float)
    """
    task = random.uniform(0, max_delay)
    await asyncio.sleep(task)
    return task
