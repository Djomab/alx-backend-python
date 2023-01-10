#!/usr/bin/env python3
"""async_comprehension"""
from typing import Generator
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """collect 10 random numbers using an async comprehensing
     then return the 10 random numbers.
    """
    return [i async for i in async_generator()]
