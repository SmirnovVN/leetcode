from collections import defaultdict
from heapq import heappop, heappush
from math import inf

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move(matrix, pico, max_cheats):
    m, n = len(matrix), len(matrix[0])

    q = []
    sx = sy = ex = ey = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'S':
                sx, sy = j, i
                q.append((0, 0, j, i, 0, None))
                matrix[i][j] = '.'
            if matrix[i][j] == 'E':
                ex, ey = j, i
                matrix[i][j] = '.'
    def h(hx, hy):
        return abs(hx - ex) + abs(hy - ey)

    visited = [[defaultdict(lambda: inf) for _ in range(n)] for _ in range(m)]
    wocheats = inf
    result = defaultdict(list)
    while q:
        _, path, x, y, cheats, ch_start = heappop(q)
        if path > wocheats - pico:
            continue
        visited[y][x][ch_start] = min(path, visited[y][x][ch_start])
        if (x, y) == (ex, ey) and path <= wocheats - pico:
            if wocheats < inf:
                result[ch_start].append(path)
            else:
                wocheats = path
                q = [(0, 0, sx, sy, max_cheats, None)]
                # visited = [[defaultdict(lambda: inf) for _ in range(n)] for _ in range(m)]
                continue
        for d in directions:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < n and 0 <= ny < m and (cheats > 0 or visited[ny][nx][None] - pico >= path + 1):
                if matrix[ny][nx] == '.' and visited[ny][nx][ch_start] >= path + 1:
                    if cheats != max_cheats:
                        ncheats = 0
                    else:
                        ncheats = cheats
                    heappush(q, (path + 1 + h(nx, ny), path + 1, nx, ny, ncheats, ch_start))
                elif matrix[ny][nx] == '#' and cheats > 0:
                    if cheats == max_cheats:
                        nch_start = (nx, ny)
                    else:
                        nch_start = ch_start
                    if visited[ny][nx][nch_start] >= path + 1:
                        heappush(q, (path + 1 + h(nx, ny), path + 1, nx, ny, cheats - 1, nch_start))
    print(result)
    return len(result)



def parse(file):
    result = []
    for line in file:
        result.append(list(line.strip()))
    return result



if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('test_3.txt') as file:
        test_3 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)
    #
    res = move(test_1, 20, 1)
    print(res)
    assert res == 5

    res = move(inp, 100, 1)
    print(res)

    res = move(test_1, 50, 20)
    print(res)
    assert res == 285

    res = move(inp, 100, 20)
    print(res)

# 1839 - too high
# 1445