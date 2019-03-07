from typing import List


def reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)


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
