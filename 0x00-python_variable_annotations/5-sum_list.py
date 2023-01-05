#!/usr/bin/env python3
''' type-annotated function sum_list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Args:
        input_list: float
    Return:
        sum float.
    '''
    sum: int = 0
    for x in input_list:
        sum += x
    return sum
