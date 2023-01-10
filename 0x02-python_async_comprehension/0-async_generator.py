#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments."""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """no arguments
    Return:
        Random number between 0 and 10
    """
    for i in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
