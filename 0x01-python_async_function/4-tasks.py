#!/usr/bin/env python3
"""
Import wait_random from the previous python file and write an async routine
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine to spawn task_wait_random n times with the specified max_delay
    Returns a list of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
