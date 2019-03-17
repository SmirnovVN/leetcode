from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def _climb(rem):
            result = 0
            if rem >= 2:
                result += _climb(rem - 2)
            if rem >= 1:
                result += _climb(rem - 1)
            if rem == 0:
                result += 1

            return result

        return _climb(n)


if __name__ == '__main__':
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(7) == 21
