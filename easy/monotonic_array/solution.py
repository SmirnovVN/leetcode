from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        mono = None
        prev = A[0]
        for i in range(1, len(A)):
            if mono is None:
                if A[i] > prev:
                    mono = True
                elif A[i] < prev:
                    mono = False
            elif mono:
                if A[i] < prev:
                    return False
            else:
                if A[i] > prev:
                    return False
            prev = A[i]
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isMonotonic([1, 2, 2, 3])
    assert s.isMonotonic([6, 5, 4, 4])
    assert not s.isMonotonic([1, 3, 2])
    assert s.isMonotonic([1, 2, 4, 5])
    assert s.isMonotonic([1, 1, 1])
