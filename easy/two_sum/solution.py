from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_add = {}
        for i, num in enumerate(nums):
            if num in to_add:
                return [to_add[num], i]
            else:
                to_add[target - num] = i


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
