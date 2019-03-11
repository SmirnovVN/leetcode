from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right + 1) // 2
            if nums[m] == target:
                return m
            elif nums[left] <= target <= nums[m] or nums[m] <= nums[left] <= target or target <= nums[m] <= nums[left]:
                right = m - 1
            else:
                left = m + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
