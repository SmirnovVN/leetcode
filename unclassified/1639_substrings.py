class Solution:
    def numWays(self, words: [str], target: str) -> int:
        n, chars = len(words[0]), len(target)

        mod = 10 ** 9 + 7

        dp = [0] * (chars + 1)
        dp[0] = 1

        cnt = [[0] * 26 for _ in range(n)]
        for j in range(n):
            for w in words:
                cnt[j][ord(w[j]) - ord('a')] += 1

        for j in range(n):
            for k in range(chars - 1, -1, -1):
                dp[k + 1] += dp[k] * cnt[j][ord(target[k]) - ord('a')]
                dp[k + 1] %= mod

        return dp[chars]

if __name__ == '__main__':
    s = Solution()
    words = ["acca","bbbb","caca"]
    target = "aba"
    print(s.numWays(words, target))
    assert s.numWays(words, target) == 6
