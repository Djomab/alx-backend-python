#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10):
    rand = random.random() * max_delay
    await asyncio.sleep(rand)
    return rand
