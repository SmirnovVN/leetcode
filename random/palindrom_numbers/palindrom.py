def palindrom_count(x):
    counter = 1
    res = 0
    while counter <= x:
        if is_palindrom(counter):
            res += 1
        counter += 1
    return res


def is_palindrom(x):
    lst = str(x)
    return lst == lst[::-1]


assert 13 == palindrom_count(50)
