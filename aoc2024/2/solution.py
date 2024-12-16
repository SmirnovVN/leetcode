def is_safe(levels):
    if levels[0] < levels[1]:
        bounds = [1, 3]
    else:
        bounds = [-3, -1]

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if diff < bounds[0] or diff > bounds[1]:
            return False

    return True

def is_safe2(levels):
    safe = asc = 0
    diffs = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
    for diff in diffs:
        if diff > 0:
            asc += 1

    n = len(diffs)

    if asc >= n - 1:
        bounds = [1, 3]
    elif asc <= 1:
        bounds = [-3, -1]
    else:
        return False

    prev = levels[0]
    for cur in levels[1:]:
        diff = cur - prev
        if bounds[0] <= diff <= bounds[1]:
            safe += 1
            prev = cur

    return safe >= n - 1



def count_safe(matrix):
    result = 0
    result2 = 0
    for levels in matrix:
        if is_safe(levels):
            result += 1
        if is_safe2(levels) or is_safe2(levels[::-1]):
            result2 += 1

    return result, result2


def parse(data):
    m = []
    for line in data:
        s = line.split(' ')
        m.append(list(map(int, s)))

    return m

if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = count_safe(test_1)
    print(res)
    assert res == (2, 4)

    res = count_safe(test_2)
    print(res)
    assert res == (3, 14)

    res = count_safe(inp)
    print(res)
