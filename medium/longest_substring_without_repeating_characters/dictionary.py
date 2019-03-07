class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        result = 1
        window = 0
        char_last_indices = {}
        for i, ch in enumerate(s):
            if ch in char_last_indices and char_last_indices[ch] >= window:
                window = char_last_indices[ch] + 1
            size = i - window + 1
            if size > result:
                result = size
            char_last_indices[ch] = i
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthOfLongestSubstring('abcabcbb') == 3
    assert sol.lengthOfLongestSubstring('bbbbb') == 1
    assert sol.lengthOfLongestSubstring('pwwkew') == 3
