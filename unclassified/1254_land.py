class Graph:
    def __init__(self, m, n):
        self.parents = [[None] * n for _ in range(m)]
        self.ranks = [[0] * n for _ in range(m)]

    def parent(self, node):
        x, y = node
        if self.parents[x][y]:
            return self.parent((self.parents[x][y]))

        return node

    def union(self, first, second):
        first_p, second_p = self.parent(first), self.parent(second)

        if first_p == second_p:
            return
        elif self.ranks[first_p[0]][first_p[1]] < self.ranks[second_p[0]][second_p[1]]:
            self.parents[first_p[0]][first_p[1]] = second_p
        elif self.ranks[second_p[0]][second_p[1]] < self.ranks[first_p[0]][first_p[1]]:
            self.parents[second_p[0]][second_p[1]] = first_p
        else:
            self.ranks[first_p[0]][first_p[1]] += 1
            self.parents[second_p[0]][second_p[1]] = first_p


class Solution:
    def closedIsland(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])

        graph = Graph(m, n)

        for i in range(m):
            for j in range(n):
                if i + 1 < m and not (grid[i][j] or grid[i + 1][j]):
                    graph.union((i, j), (i + 1, j))
                if j + 1 < n and not (grid[i][j] or grid[i][j + 1]):
                    graph.union((i, j), (i, j + 1))

        lands = set()
        not_islands = set()

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    parent = graph.parent((i, j))
                    lands.add(parent)
                    if i in {0, m - 1} or j in {0, n - 1}:
                        not_islands.add(parent)

        return len(lands) - len(not_islands)

if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0]]
    s = Solution()
    print(s.closedIsland(grid))
