from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = left = right = 0
        prod = nums[0]
        while right < n:
            if prod < k:
                res += right - left + 1
                right += 1
                if right < n:
                    prod *= nums[right]
            else:
                if left < right:
                    prod //= nums[left]
                    left += 1
                else:
                    left = right = right + 1
                    if right < n:
                        prod = nums[left]
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
