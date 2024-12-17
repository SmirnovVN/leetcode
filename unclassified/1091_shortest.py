from collections import defaultdict
from heapq import heappop, heappush
inf = float('Inf')


class Solution:
    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1

        n = len(grid)

        def neighbours(i, j):
            if j + 1 < n and grid[i][j + 1] == 0:
                yield i, j + 1
            if j - 1 >= 0 and grid[i][j - 1] == 0:
                yield i, j - 1
            if i + 1 < n:
                if grid[i + 1][j] == 0:
                    yield i + 1, j
                if j + 1 < n and grid[i + 1][j + 1] == 0:
                    yield i + 1, j + 1
                if j - 1 >= 0 and grid[i + 1][j - 1] == 0:
                    yield i + 1, j - 1
            if i - 1 >= 0:
                if grid[i - 1][j] == 0:
                    yield i - 1, j
                if j + 1 < n and grid[i - 1][j + 1] == 0:
                    yield i - 1, j + 1
                if j - 1 >= 0 and grid[i - 1][j - 1] == 0:
                    yield i - 1, j - 1

        def h(x, y):
            return max(n - x, n - y)

        distances = defaultdict(lambda: inf)
        distances[0, 0] = 1

        q = [(1, 0, 0)]

        while q:
            _, x, y = heappop(q)
            d = distances[x, y]
            if (x, y) == (n - 1, n - 1):
                return d
            for i, j in neighbours(x, y):
                if d + 1 < distances[i, j]:
                    distances[i, j] = d + 1
                    heappush(q, (d + h(i, j), i, j))

        return -1
