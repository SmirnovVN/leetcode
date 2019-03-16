from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _permute(acc, rem):
            result = []
            if rem:
                for num in rem:
                    result += _permute(acc + [num], [item for item in rem if item != num])
            else:
                result.append(acc)
            return result

        return _permute([], nums)


if __name__ == '__main__':
    s = Solution()
    assert s.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
