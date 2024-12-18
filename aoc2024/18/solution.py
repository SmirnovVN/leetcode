from heapq import heappop, heappush
from math import inf

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move(bytes, steps, n):
    matrix = [['.']*(n + 1) for _ in range(n + 1)]
    for i, j in bytes[:steps]:
        matrix[i][j] = '#'

    def h(hx, hy):
        return 2 * n - hx - hy

    visited = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    q = [(0, 0, 0, 0)]
    while q:
        _, path, x, y = heappop(q)
        if x == y == n:
            return path
        for d in directions:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx <= n and 0 <= ny <= n and matrix[ny][nx] == '.' and visited[ny][nx] > path + 1:
                heappush(q, (path + 1 + h(nx, ny), path + 1, nx, ny))
                visited[ny][nx] = min(path + 1, visited[ny][nx])

    return -1





def parse(data):
    result = []
    for line in data:
        s = line.split(',')
        result.append((int(s[0]), int(s[1])))

    return result


def find_byte(bytes):
    i = 1024
    while move(bytes, i, 70) > 0:
        i += 1

    return bytes[i - 1]


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = move(test_1, 12, 6)
    print(res)
    assert res == 22

    res = move(inp, 1024, 70)
    print(res)

    res = find_byte(inp)
    print(res)
