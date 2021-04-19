"""
Stringsで最も多く使われている文字をカウントする
Input : strings = 'This is a pen. This is an apple. Applepen.'
Output : ('p', 6)
"""
from typing import List, Tuple
import operator
from collections import Counter


def count_chars_v1(strings: str):
    strings = strings.lower()
    l = []
    for char in strings:
        if not char.isspace():
            l.append((char, strings.count(char)))
    return max(l, key=operator.itemgetter(1))


def count_chars_v2(strings: str):
    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1  # dictionary.get(key, default値)
    max_key = max(d, key=d.get)
    return max_key, d[max_key]

def count_chars_v3(strings: str):
    strings = strings.lower()
    d = Counter()
    for char in strings:
        if not char.isspace():
            d[char] += 1  # dictionary.get(key, default値)
    # max_key = max(d, key=d.get)
    # return max_key, d[max_key]
    return d.most_common()

if __name__=='__main__':
    strings = 'This is a pen. This is an apple. Applepen. I am a great person. Yeah.'
    print(count_chars_v1(strings))
    print(count_chars_v2(strings))
    print(count_chars_v3(strings))