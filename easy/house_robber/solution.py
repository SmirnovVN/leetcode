from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev = prev = cur = 0
        for i in nums:
            prev_prev, prev, cur = prev, cur, max(i + prev, i + prev_prev)
        return max(prev, cur)


if __name__ == '__main__':
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([10, 13, 7, 1, 9, 1, 1, 3, 1]) == 29
    assert s.rob([10, 18, 7, 1, 9, 1, 1, 3, 1]) == 30
