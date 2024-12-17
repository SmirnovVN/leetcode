from typing import List


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)

        dp[1] = nums[0]

        even = nums[0] % 2 == 0
        if even:
            last_odd = 0
            last_even = 1
        else:
            last_odd = 1
            last_even = 0

        dp[0] = nums[0] - x
        for i in range(1, n):
            if nums[i] % 2:
                dp[i + 1] = max(dp[last_odd] + nums[i], dp[i] + nums[i] - (x if even else 0))
                last_odd = i + 1
                even = False
            else:
                dp[i + 1] = max(dp[last_even] + nums[i], dp[i] + nums[i] - (0 if even else x))
                last_even = i + 1
                even = True

        return max(dp)


if __name__ == '__main__':
    # s = Solution()
    # c = [2,3,6,1,9,2]
    # d = 5
    # a = s.maxScore(c, d)
    # print(a)
    # assert a == 13
    # s = Solution()
    # c = [2,4,6,8]
    # d = 3
    # a = s.maxScore(c, d)
    # print(a)
    # assert a == 20
    s = Solution()
    c = [99,88,98,15,34,40,29,81,2,6,12,9,82,93,5,81,84,71,83,31,12,22,9,65,56,9,68,79,39,84,50,7,25,3,49]
    d = 19
    a = s.maxScore(c, d)
    print(a)
    assert a == 1363


"""

"""