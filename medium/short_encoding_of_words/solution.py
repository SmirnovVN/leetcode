from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words[:] = sorted(word[::-1] for word in words)
        words.sort(key=len, reverse=True)
        bigger_words = []
        result = 0
        for word in words:
            for bigger_word in bigger_words:
                if bigger_word.startswith(word):
                    break
            else:
                bigger_words.append(word)
                result += len(word) + 1
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.minimumLengthEncoding(["time", "me", "bell"]) == 10
    assert s.minimumLengthEncoding(["time", "atime", "btime"]) == 12
