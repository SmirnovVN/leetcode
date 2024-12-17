class Solution:
    def minCost(self, n: int, cuts: [int]) -> int:
        cuts += [0, n]
        cuts.sort()
        q = [(0, len(cuts) - 1)]
        result = 0
        while q:
            start, end = q.pop()
            if start + 1 < end:
                result += cuts[end] - cuts[start]
                mid = start + (end - start) // 2
                q.append((start, mid))
                q.append((mid, end))

        return result

if __name__ == '__main__':
    s = Solution()
    n = 7
    d = [1,3,4,5]
    print(s.minCost(n, d))
    assert s.minCost(n, d) == 16