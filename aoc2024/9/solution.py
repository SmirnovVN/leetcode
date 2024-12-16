def compress(nums):
    i = 0
    disk = []
    file = True
    for num in nums:
        if file:
            disk += [i] * num
            i += 1
        else:
            disk += ['.'] * num
        file = not file

    n = len(disk)
    i, j = n - 1, disk.index('.')
    while i > 0 and disk[i] == '.':
        i -= 1

    while j < i:
        if disk[i] == '.':
            i -= 1
        else:
            disk[i], disk[j] = disk[j], disk[i]
            while j < len(disk) and disk[j] != '.':
                j += 1

    result = 0

    for i, num in enumerate(disk):
        if num != '.':
            result += i * num

    return result

def compress2(nums):
    D = [(None if i % 2 else i // 2, d) for i, d in enumerate(nums)]
    for i in range(len(D) - 1, -1, -1):
        for j in range(i):
            i_data, i_size = D[i]
            j_data, j_size = D[j]

            if i_data != None and j_data == None and i_size <= j_size:
                D[i] = (None, i_size)
                D[j] = (None, j_size - i_size)
                D.insert(j, (i_data, i_size))

    flatten = lambda x: [x for x in x for x in x]
    D = [[data if data else 0] * size for data, size in D]

    return sum(i * c for i, c in enumerate(flatten(D)) if c)


def parse(data):
    for line in data:
        return list(map(int, line.strip()))


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = compress(test_1)
    print(res)
    assert res == 1928

    res = compress(test_2)
    print(res)
    assert res == 60

    res = compress(inp)
    print(res)

    res = compress2(test_1)
    print(res)
    assert res == 2858

    res = compress2(test_2)
    print(res)
    assert res == 132

    res = compress2(inp)
    print(res)

