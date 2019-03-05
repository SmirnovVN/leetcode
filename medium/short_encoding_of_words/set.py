from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)


if __name__ == '__main__':
    s = Solution()
    assert s.minimumLengthEncoding(["time", "me", "bell"]) == 10
    assert s.minimumLengthEncoding(["time", "atime", "btime"]) == 12
