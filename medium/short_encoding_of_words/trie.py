from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = dict()
        leaves = []
        for word in set(words):
            cur = root
            for i in word[::-1]:
                cur[i] = cur = cur.get(i, dict())
            leaves.append((cur, len(word) + 1))
        return sum(depth for node, depth in leaves if len(node) == 0)


if __name__ == '__main__':
    s = Solution()
    assert s.minimumLengthEncoding(["time", "me", "bell"]) == 10
    assert s.minimumLengthEncoding(["time", "atime", "btime", "btime"]) == 12
