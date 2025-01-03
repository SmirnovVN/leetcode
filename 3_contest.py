class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7
        max_num = int(n ** (1.0 / x)) + 1

        dp = [[0 for _ in range(n + 1)] for _ in range(max_num + 1)]

        for i in range(max_num + 1):
            dp[i][0] = 1

        for i in range(1, max_num + 1):
            for j in range(1, n + 1):
                if j < i ** x:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - i ** x]) % mod

        return dp[max_num][n]


if __name__ == '__main__':
    # s = Solution()
    # c = 10
    # d = 2
    # a = s.numberOfWays(c, d)
    # print(a)
    # assert a == 1
    # s = Solution()
    # c = 4
    # d = 1
    # a = s.numberOfWays(c, d)
    # print(a)
    # assert a == 2
    # s = Solution()
    # c = 2
    # d = 1
    # a = s.numberOfWays(c, d)
    # print(a)
    # assert a == 1
    # s = Solution()
    # c = 2
    # d = 2
    # a = s.numberOfWays(c, d)
    # print(a)
    # assert a == 0
    s = Solution()
    c = 5
    d = 1
    a = s.numberOfWays(c, d)
    print(a)
    assert a == 3


"""

"""