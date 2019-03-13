from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = nums[0]
        cur = 0
        for num in nums:
            cur += num
            if cur > result:
                result = cur
            if cur < 0:
                cur = 0

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
