#!/usr/bin/env python3
''' type-annotated function sum_mixed_list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Args:
        mxd_lst: float
    Return:
        sum float.
    '''
    sum: float = 0
    for x in mxd_lst:
        sum += x
    return sum
