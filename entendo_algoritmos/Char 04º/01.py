def sum_recursion(numbers: list, _sum: int = 0) -> int:
    if len(numbers) == 0:
        return _sum

    _sum += numbers.pop()
    return sum_recursion(numbers, _sum)


def max_number_recursion(numbers: list, _max: int = 0) -> int:
    if len(numbers) == 0:
        return _max

    to_check = numbers.pop()

    if _max < to_check:
        _max = to_check

    return max_number_recursion(numbers, _max)


l = [1, 3, 5, 6, 5, 7, 89, 1, 3]

print(sum_recursion(l[:]))  # Used to make an copy of the list. The recursion
print(max_number_recursion(l[:]))  # overwrites the list.
