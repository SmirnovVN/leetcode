from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        n, m = len(s), len(p)
        if m - p.count('*') > n:
            return False
        while i < n and j < m:
            if s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            elif p[j] == '*':
                while j < m and p[j] == '*':
                    j += 1
                if j < m and p[j] != '?':
                    find_next = s.find(p[j], i)
                    while find_next != -1:
                        if self.isMatch(s[find_next:], p[j:]):
                            return True
                        if find_next + 1 < n:
                            find_next = s.find(p[j], find_next + 1)
                        else:
                            break
                    return False
                elif j < m and p[j] == '?':
                    res = False
                    while i < n:
                        res |= self.isMatch(s[i:], p[j:])
                        i += 1
                    return res
                else:
                    return True
            else:
                return False
        return i == n and (j == m or (p[j:].strip('*') == ''))


if __name__ == '__main__':
    sol = Solution()
    assert not sol.isMatch('aa', 'a')
    assert sol.isMatch('aa', '*')
    assert not sol.isMatch('cb', '?a')
    assert sol.isMatch('adceb', '*a*b')
    assert not sol.isMatch('acdcb', 'a*c?b')
    assert sol.isMatch('c', '*?*')
    assert sol.isMatch('abbbbbc', 'a*bbc')
    assert sol.isMatch('aaaaaa', 'a****')
