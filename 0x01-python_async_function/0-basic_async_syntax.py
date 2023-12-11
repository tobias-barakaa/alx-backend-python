#!/usr/bin/env python3
"""
Python function to print
"""
import asyncio
import random

async def wait_random(max_delay = 10):
    """
    funtion that return
    random value(float)
    """
    task = asyncio.sleep(random.uniform(0, max_delay))
    return await task
