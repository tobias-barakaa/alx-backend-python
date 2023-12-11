#!/usr/bin/env python3
"""
python function
"""
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function syntax that returns an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
