class Solution:
    def countPaths(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # directions = [x for x in product((-1, 0, 1), repeat=2) if x != (0, 0)]

        def neighbours(i, j):
            for di, dj in directions:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < m and 0 <= prev_j < n:
                    yield prev_i, prev_j

        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            result = 1

            for ni, nj in neighbours(i, j):
                if grid[ni][nj] < grid[i][j]:
                    result += dfs(ni, nj) % mod

            dp[i][j] = result
            return result

        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod

