def to_pins(matrix):
    m, n = len(matrix), len(matrix[0])
    result = []
    for j in range(n):
        if matrix[0][0] == '#':
            res = 0
            d = 1
        else:
            res = m - 2
            d = -1
        for i in range(1, m):
            if matrix[i][j] == matrix[0][0]:
                res += d
        result.append(res)

    return result


def keys_and_locks(data):
    keys, locks = [], []
    for m in data:
        if m[0][0] == '#':
            locks.append(to_pins(m))
        else:
            keys.append(to_pins(m))

    return keys, locks


def fit(key, lock, m):
    for k, o in zip(key, lock):
        if k + o > m - 2:
            return False

    return True


def count_pairs(data):
    result = 0

    keys, locks = keys_and_locks(data)
    for key in keys:
        for lock in locks:
            if fit(key, lock, len(data[0])):
                result += 1

    return result


def parse(data):
    result = []
    cur = []
    for line in data:
        if line == '\n':
            result.append(cur)
            cur = []
        else:
            cur.append(list(line.strip()))

    result.append(cur)
    return result


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = count_pairs(test_1)
    print(res)
    assert res == 3

    res = count_pairs(inp)
    print(res)
