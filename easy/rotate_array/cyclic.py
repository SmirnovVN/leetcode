from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        start = count = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_index = (current + k) % n
                nums[next_index], prev = prev, nums[next_index]
                current = next_index
                count += 1
                if start == current:
                    break
            start += 1


if __name__ == '__main__':
    s = Solution()
    test = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(test, 3)
    assert test == [5, 6, 7, 1, 2, 3, 4]
    test = [-1, -100, 3, 99]
    s.rotate(test, 2)
    assert test == [3, 99, -1, -100]
    test = [1, 2, 3]
    s.rotate(test, 4)
    assert test == [3, 1, 2]
    test = [1, 2, 3, 4, 5, 6]
    s.rotate(test, 4)
    assert test == [3, 4, 5, 6, 1, 2]
    test = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(test, 4)
    assert test == [4, 5, 6, 7, 1, 2, 3]
    test = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(test, 5)
    assert test == [3, 4, 5, 6, 7, 1, 2]
