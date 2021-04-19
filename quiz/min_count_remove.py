"""
2つのリストを比較し、要素数の少ない方をを削除する
x = [1, 1 ,2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 9]
y = [1, 1 ,1, 1, 2, 2, 3, 3, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9]
"""
from collections import Counter

def min_count_remove(x:list, y:list) -> None:
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x > value_y:
                y[:] = [i for i in y if i != key_x]
            elif value_x < value_y:
                x[:] = [i for i in x if i != key_x]

if __name__=='__main__':
    x = [1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 9]
    y = [1, 1, 1, 1, 2, 2, 3, 3, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9]
    print('x : ', x)
    print('y : ', y)
    min_count_remove(x,y)
    print('x : ', x)
    print('y : ', y)