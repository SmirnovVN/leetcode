from collections import defaultdict


def cnt_antinodes(data):
    m, n = len(data), len(data[0])

    nodes = defaultdict(list)
    antinodes = set()
    for i in range(m):
        for j in range(n):
            if data[i][j] != '.':
                for x, y in nodes[data[i][j]]:
                    for ax, ay in ((2 * i - x, 2 * j - y), (2 * x - i, 2 * y - j)):
                        if 0 <= ax < m and 0 <= ay < n:
                            antinodes.add((ax, ay))
                nodes[data[i][j]].append((i, j))

    return len(antinodes)


def cnt_antinodes2(data):
    m, n = len(data), len(data[0])

    nodes = defaultdict(list)
    antinodes = set()
    for i in range(m):
        for j in range(n):
            if data[i][j] not in {'.', '#'}:
                for x, y in nodes[data[i][j]]:
                    antinodes.add((i, j))
                    antinodes.add((x, y))
                    repeat = True
                    k = 0
                    while repeat:
                        k += 1
                        repeat = False
                        for ax, ay in (((k + 1) * i - k * x, (k + 1) * j - k * y), ((k + 1) * x - k * i, (k + 1) * y - k * j)):
                            if 0 <= ax < m and 0 <= ay < n:
                                antinodes.add((ax, ay))
                                repeat = True
                nodes[data[i][j]].append((i, j))

    return len(antinodes)


def parse(data):
    result = []
    for line in data:
        result.append(list(line.strip()))

    return result

if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = cnt_antinodes(test_1)
    print(res)
    assert res == 14

    res = cnt_antinodes(inp)
    print(res)

    res = cnt_antinodes2(test_1)
    print(res)
    assert res == 34

    res = cnt_antinodes2(inp)
    print(res)

