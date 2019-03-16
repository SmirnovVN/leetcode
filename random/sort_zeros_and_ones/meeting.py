def sort(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] == 0:
            left += 1
        if lst[right] == 1:
            right -= 1
        elif lst[left] == 1:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

    return lst


assert [0, 1] == sort([0, 1])
assert [0, 0, 1] == sort([0, 1, 0])
assert [0, 0, 1, 1, 1] == sort([0, 1, 0, 1, 1])
assert [0, 0, 0, 0, 1] == sort([0, 1, 0, 0, 0])
