from heapq import heappop, heappush

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move(matrix, pico, max_cheats):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'S':
                si, sj = i, j
            elif matrix[i][j] == 'E':
                ei, ej = i, j

    def bfs(si, sj, ei, ej):
        q = []
        heappush(q, (0, si, sj))
        dist = {}
        best = None

        while q:
            sc, ci, cj = heappop(q)

            if (ci, cj) not in dist:
                dist[(ci, cj)] = sc
            else:
                continue

            if ci == ei and cj == ej:
                best = sc

            for d in directions:
                ni, nj = ci + d[0], cj + d[1]
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] != '#':
                    heappush(q, (sc + 1, ni, nj))

        return dist, best

    def step_distance(a, b):  # manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    distances_start, best_no_cheat = bfs(si, sj, ei, ej)
    distances_end, _ = bfs(ei, ej, si, sj)

    result = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '#' or (i, j) not in distances_start:
                continue
            for k in range(max(i - max_cheats, 0), min(i + max_cheats, m - 1) + 1):
                for o in range(max(j - max_cheats, 0), min(j + max_cheats, n - 1) + 1):
                    sd = step_distance((i, j), (k, o))
                    if sd > max_cheats or matrix[k][o] == '#' or (k, o) not in distances_end:
                        continue
                    dist = distances_start[(i, j)] + distances_end[(k, o)] + sd

                    if dist <= best_no_cheat - pico:
                        result += 1

    return result


def parse(file):
    result = []
    for line in file:
        result.append(list(line.strip()))
    return result



if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = move(test_1, 20, 2)
    print(res)
    assert res == 5

    res = move(inp, 100, 2)
    print(res)

    res = move(test_1, 50, 20)
    print(res)
    assert res == 285

    res = move(inp, 100, 20)
    print(res)
