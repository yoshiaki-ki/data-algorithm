"""
cacheを作成する
"""

import time
from functools import lru_cache

def memoize(f):
    cache = {}
    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper

# @lru_cache()  # lru_cacheを用いる場合
# def long_calc(num:int):
#     r = 0
#     for i in range(10000000):
#         r += i * num
#     return r

@memoize  # lru_cacheを用いる場合
def long_calc(num:int):
    r = 0
    for i in range(10000000):
        r += i * num
    return r


if __name__=='__main__':
    for i in range(10):
        print(long_calc(i))

    start = time.time()
    for i in range(10):
        print(long_calc(i))
    print(time.time()-start)