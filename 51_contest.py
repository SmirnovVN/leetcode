class Solution:
    def minExtraChar(self, s: str, dictionary: [str]) -> int:
        n = len(s)

        dp = list(range(n + 1))
        start = 0
        while start < n:
            candidates = set(dictionary)
            end = start
            while end < n and candidates:
                new_candidates = set()
                end += 1
                for cand in candidates:
                    if s[start:end] == cand:
                        dp[end] = min(dp[end], dp[end - 1] + 1, dp[start])
                    elif s[start:end] in cand:
                        new_candidates.add(cand)
                candidates = new_candidates
            start += 1
            dp[start] = min(dp[start], dp[start - 1] + 1)

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    c = "leetscode"
    d = ["leet","code","leetcode"]
    print(s.minExtraChar(c, d))
    assert s.minExtraChar(c, d) == 1
    c = "sayhelloworld"
    d = ["hello","world", "a", "o", "he"]
    print(s.minExtraChar(c, d))
    assert s.minExtraChar(c, d) == 2
    c = "sayhelloworld"
    d = ["hello","world"]
    print(s.minExtraChar(c, d))
    assert s.minExtraChar(c, d) == 3
    c = "dwmodizxvvbosxxw"
    d = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
    print(s.minExtraChar(c, d))
    assert s.minExtraChar(c, d) == 7

"""
"leetscode"
["leet","code","leetcode"]
"sayhelloworld"
["hello","world"]
"sayhelloworld"
["hello","world", "a", "o", "he"]
"dwmodizxvvbosxxw"
["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
"""
