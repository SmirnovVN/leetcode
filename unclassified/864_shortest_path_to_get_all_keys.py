from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def neighbours(i, j):
            for di, dj in directions:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] != '#':
                    yield prev_i, prev_j

        items = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] not in {'#', '.', '@'}:
                    items[grid[i][j]] = (i, j)
                if grid[i][j] == '@':
                    start = (i, j)

        keys = (len(items)) // 2

        def h(i, j, d, k):
            for key, (x, y) in items.items():
                if key > 'Z':
                    if key not in k:
                        d += abs(x - i) + abs(y - j)
            return d

        start_h = h(start[0], start[1], 0, set())
        q = [(start_h, 0, set(), start)]
        min_h = defaultdict(lambda : [[inf] * n for _ in range(m)])
        min_h[0][start[0]][start[1]] = start_h
        result = inf
        while q:
            _, d, k, (x, y) = heappop(q)
            if len(k) == keys:
                result = min(result, d)
            for i, j in neighbours(x, y):
                cur_k = k
                if grid[i][j] in items:
                    if grid[i][j] <= 'Z':
                        if grid[i][j].lower() not in cur_k:
                            continue
                    else:
                        cur_k = cur_k.copy()
                        cur_k.add(grid[i][j])
                cur_h = h(i, j, d + 1, cur_k)
                kk = tuple(sorted(cur_k))
                if min_h[kk][i][j] > cur_h:
                    heappush(q, (cur_h, d + 1, cur_k, (i, j)))
                    min_h[kk][i][j] = cur_h

        return result if result < inf else -1

if __name__ == '__main__':
    s = Solution()
    # c = ["@.a..","###.#","b.A.B"]
    # assert s.shortestPathAllKeys(c) == 8
    c = [".#.b.","A.#aB","#d...","@.cC.","D...#"]
    a = s.shortestPathAllKeys(c)
    print(a)
    assert a == 8
    c = ["@...a",".###A","b.BCc"]
    a = s.shortestPathAllKeys(c)
    print(a)
    assert a == 10
    c = ["..#....##.","....d.#.D#","#...#.c...","..##.#..a.","...#....##","#....b....",".#..#.....","..........",".#..##..A.",".B..C.#..@"]
    a = s.shortestPathAllKeys(c)
    print(a)
    assert a == 19