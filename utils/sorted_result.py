from collections import Counter
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])

        left, right = 0, 0
        q = len(queries)
        result = [0]*q
        cnt = Counter()
        for i in sorted(range(q), key=lambda x: queries[x]):
            while right < len(logs) and logs[right][1] <= queries[i]:
                cnt[logs[right][0]] += 1
                right += 1
            while left < len(logs) and logs[left][1] < queries[i] - x:
                cnt[logs[left][0]] -= 1
                if cnt[logs[left][0]] == 0: del cnt[logs[left][0]]
                left += 1
            result[i] = n - len(cnt)

        return result
