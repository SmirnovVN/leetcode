from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        n = len(A)
        while even < n and odd < n:
            if A[even] % 2 == 0:
                even += 2
            else:
                if A[odd] % 2 == 1:
                    odd += 2
                elif A[odd] % 2 < A[even] % 2:
                    A[odd], A[even] = A[even], A[odd]
                    even += 2
                    odd += 2
        return A


if __name__ == '__main__':
    s = Solution()
    assert s.sortArrayByParityII([4, 2, 5, 7]) == [4, 5, 2, 7]
