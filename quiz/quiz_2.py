"""
1. 与えられたリストの要素を足して、指定された値を作成するには？
Input: [11,2,5,9,10,3], 12 -> Output: (2, 10) or None

2. 与えられたリストの要素で和が同じになるような組み合わせはあるか？
Input: [11,2,5,9,10,3] -> Output: (11,9) or None
"""

from typing import List, Tuple, Optional


def get_pair(numbers: List, target: int) -> Optional:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_pair_half_sum(numbers: List) -> Optional:
    sum_num = sum(numbers)
    half_sum, remainder = divmod(sum_num, 2)
    if remainder != 0:
        return

    cache = set()
    for num in numbers:
        val = half_sum - num
        if val in cache:
            return val, num
        cache.add(num)


if __name__ == '__main__':
    numbers = [11, 2, 5, 9, 10, 3]
    print(get_pair_half_sum(numbers))
