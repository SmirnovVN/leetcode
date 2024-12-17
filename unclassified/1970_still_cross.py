from itertools import product
from typing import List


class UnionFind:
    def __init__(self, m, n):
        self.parent = [[None] * n for _ in range(m)]
        self.rank = [[1] * n for _ in range(m)]

    def find(self, node):
        i, j = node
        if self.parent[i][j]:
            return self.find(self.parent[i][j])
        return node

    def union(self, fst, snd):
        (fi, fj), (si, sj) = self.find(fst), self.find(snd)

        if (fi, fj) == (si, sj):
            return
        if self.rank[fi][fj] > self.rank[si][sj]:
            (fi, fj), (si, sj) = (si, sj), (fi, fj)
        self.rank[si][sj] += self.rank[fi][fj]
        self.parent[fi][fj] = (si, sj)


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0] * col for _ in range(row)]
        uf = UnionFind(row, col)

        left, right = (row, 0), (row, 1)
        uf.parent.append([None, None])
        uf.rank.append([1, 1])

        directions = [x for x in product((-1, 0, 1), repeat=2) if x != (0, 0)]

        def neighbours(i, j):
            for di, dj in directions:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < row and 0 <= prev_j < col and grid[prev_i][prev_j]:
                    yield prev_i, prev_j
            if j == 0:
                yield left
            if j == col - 1:
                yield right

        for index, (r, c) in enumerate(cells):
            r, c = r - 1, c - 1
            grid[r][c] = 1
            for i, j in neighbours(r, c):
                uf.union((i, j), (r, c))
            if uf.find(left) == uf.find(right):
                return index

        return len(cells)


if __name__ == '__main__':
    s = Solution()
    c = 2
    d = 2
    e = [[1, 1], [2, 1], [1, 2], [2, 2]]
    a = s.latestDayToCross(c, d, e)
    print(a)
    assert a == 2
