def sort(lst):
    n = len(lst)
    i = 0
    while i < n:
        if lst[i] == 0:
            i += 1
        else:
            break
    j = i + 1
    while j < n:
        if lst[j] == 1:
            j += 1
        else:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j += 1

    return lst


assert [0, 1] == sort([0, 1])
assert [0, 0, 1] == sort([0, 1, 0])
assert [0, 0, 1, 1, 1] == sort([0, 1, 0, 1, 1])
assert [0, 0, 0, 0, 1] == sort([0, 1, 0, 0, 0])
