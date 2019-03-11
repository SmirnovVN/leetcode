import itertools


class Solution:
    def clumsy(self, N: int) -> int:
        op = itertools.cycle(['*', '//', '+', '-'])
        return eval(''.join(str(n) + next(op) if n != 1 else str(n) for n in range(N, 0, -1)))


if __name__ == '__main__':
    s = Solution()
    assert s.clumsy(4) == 7
    assert s.clumsy(10) == 12
