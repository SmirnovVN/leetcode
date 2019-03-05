class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        if m - p.count('*') > n:
            return False

        i = j = 0
        star = match = None

        while i < n:
            if j < m and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < m and p[j] == '*':
                star = j
                j += 1
                match = i
            elif star is not None:
                j = star + 1
                match += 1
                i = match

            else:
                return False

        return p[j:].strip('*') == ''


if __name__ == '__main__':
    sol = Solution()
    assert not sol.isMatch('aa', 'a')
    assert sol.isMatch('aa', '*')
    assert not sol.isMatch('cb', '?a')
    assert sol.isMatch('adceb', '*a*b')
    assert not sol.isMatch('acdcb', 'a*c?b')
    assert sol.isMatch('c', '*?*')
    assert sol.isMatch('abbbbbc', 'a*bbc')
    assert sol.isMatch('abbbbbccccc', 'a*bbc*cc')
    assert sol.isMatch('aaaaaa', 'a****')
