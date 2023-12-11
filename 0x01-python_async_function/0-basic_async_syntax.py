#!/usr/bin/env python3
"""
Python function to print
"""
import asyncio
import random

def wait_random(max_delay = 10):
    """
    funtion that return
    random value(float)
    """
    return await asyncio.sleep(random.uniform(0, max_delay))
