"""
Symmetric: 左右対称のものを出力する
Input [(1,2), (3,5), (4,7), (5,3), (7,4)]
Output [(3,5), (4,7)]
"""

from typing import List, Iterator, Tuple

def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int,int]]:
    cache = {}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
            print('cache = ',cache)
        elif value == first:
            yield pair

if __name__=='__main__':
    pairs = [(1,2), (3,5), (4,7), (5,3), (7,4), (6,7), (4,5), (7,4)]
    for p in find_pair(pairs):
        print(p)