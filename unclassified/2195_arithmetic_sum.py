class Solution:
    def minimalKSum(self, nums, k) -> int:
        diff = 0
        diff_cache = set()
        for i in sorted(nums):
            if i <= k:
                if i not in diff_cache:
                    k += 1
                    diff += i
                    diff_cache.add(i)
            else:
                break

        return int(k * (k + 1) / 2) - diff


if __name__ == '__main__':
    s = Solution()
    mt = [1,2,3,4,5,5,6]
    print(s.minimalKSum(mt, 6))
