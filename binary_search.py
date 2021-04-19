from typing import List


def linear_search(numbers: List[int], value: int) -> int:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
        return -1


def binary_search(numbers: List[int], value: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 再帰関数
def recursible_binary_search(numbers: List[int], value: int) -> int:
    def _recursible_binary_search(numbers, value, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _recursible_binary_search(numbers, value, mid + 1, right)
        else:
            return _recursible_binary_search(numbers, value, left, mid - 1)

    return _recursible_binary_search(numbers, value, 0, len(numbers) - 1)


if __name__ == '__main__':
    # import random
    # numbers = [random.randint(0,1000) for _ in range(10)]
    nums = [2, 4, 12, 26, 34, 44, 52, 67, 73, 84, 99]
    print(recursible_binary_search(nums, 99))
    print(binary_search(nums, 12))
