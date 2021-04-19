"""
[1, 2, 3] -> 124
[2, 3] -> 24
[7, 8, 9] -> 790
[9, 9, 9] -> 1000
[0, 0, 0, 9, 9, 9] -> 1000

"""

def list_to_int(numbers):
    i = len(numbers) - 1
    sum = 0
    for i, num in enumerate(reversed(numbers)):
        sum += num * (10 ** i)
    return sum

def remove_zero(numbers: list):
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)
    return numbers


def list_to_int_plus_one(numbers: list) -> int:
    # リストの後ろから見ていく
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        # 7, 8, 9 -> 7, 8, 10 -> 7, 9, 0
        numbers[i] = 0
        numbers[i - 1] += 1

        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)
        i -= 1

    return list_to_int(numbers)


if __name__ == '__main__':
    print(list_to_int_plus_one([1, 2, 3]))
    print(list_to_int_plus_one([7, 9, 9]))
    print(list_to_int_plus_one([0, 0, 0, 0, 7, 9, 9]))
    print(list_to_int_plus_one([1, 3, 9]))
    print(list_to_int_plus_one([0, 0, 9, 9, 9]))
