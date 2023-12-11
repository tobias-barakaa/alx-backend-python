#!/usr/bin/env python3
"""
import function and use it
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random
"""
function that return
list of functions
"""


async def max_delay(n: int, max_delay: int) -> List[float]:
    delays = [await wait_random(max_delay) for _ in range(n)]
    delays.sort()
    return delays