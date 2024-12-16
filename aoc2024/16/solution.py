from heapq import heappop, heappush
from math import inf

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move(matrix):
    m, n = len(matrix), len(matrix[0])

    q = []
    ex, ey = 1, n - 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'S':
                q.append((0, 0, 0, {(j, i)}, j, i))
                matrix[i][j] = '.'
            if matrix[i][j] == 'E':
                ex, ey = j, i
                matrix[i][j] = '.'
    def h(hx, hy):
        return abs(hx - ex) + abs(hy - ey)
    visited = [[[inf]*4 for _ in range(n)] for _ in range(m)]
    result = inf
    places = set()
    while q:
        _, score, d, path, x, y = heappop(q)
        visited[y][x][d] = min(score, visited[y][x][d])
        if (x, y) == (ex, ey) and score <= result:
            result = score
            places.update(path)
        nx, ny = x + directions[d][1], y + directions[d][0]
        if 0 <= nx < n and 0 <= ny < m and matrix[ny][nx] == '.' and visited[ny][nx][d] >= score + 1:
            npath = path.copy()
            npath.add((nx, ny))
            heappush(q, (score + 1 + h(nx, ny), score + 1, d, npath, nx, ny))

        rd, ld = (d + 1) % 4, (4 + d - 1) % 4
        if visited[y][x][rd] >= score + 1000:
            heappush(q, (score + 1000 + h(x, y), score + 1000, rd, path.copy(), x, y))
        if visited[y][x][ld] >= score + 1000:
            heappush(q, (score + 1000 + h(x, y), score + 1000, ld, path.copy(), x, y))

    return result, len(places)



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

    res = move(test_1)
    print(res)
    assert res == (7036, 45)

    res = move(test_2)
    print(res)
    assert res == (11048, 64)

    res = move(inp)
    print(res)
