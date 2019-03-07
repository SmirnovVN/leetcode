class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        result = 1
        window = 0
        for i in range(len(s)):
            for j in range(window, i):
                if s[j] == s[i]:
                    window = j + 1
                    break
            else:
                size = i - window + 1
                if size > result:
                    result = size

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('pwwkew') == 3
