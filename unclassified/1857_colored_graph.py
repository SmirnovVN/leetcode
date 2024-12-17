from collections import defaultdict, deque


class Solution:
    def largestPathValue(self, colors: str, edges: [[int]]) -> int:
        result = -1
        n = len(colors)
        lengths = [None] * n
        visited = 0

        parents = [[] for _ in range(n)]
        children = [[] for _ in range(n)]

        for e in edges:
            if e[0] == e[1]:
                return -1

            parents[e[1]].append(e[0])
            children[e[0]].append(e[1])

        queue = deque()

        for i, c in enumerate(children):
            if not c:
                queue.append((i, -1))

        waitlist = set()
        while queue:
            cur, vis = queue.popleft()
            if vis < visited:
                for ch in children[cur]:
                    if not lengths[ch]:
                        queue.append((cur, visited))
                        waitlist.add(cur)
                        break
                else:
                    length = defaultdict(int)
                    for ch in children[cur]:
                        for k, v in lengths[ch].items():
                            length[k] = max(length[k], v)
                    length[colors[cur]] += 1
                    result = max(result, length[colors[cur]])
                    lengths[cur] = length
                    for p in parents[cur]:
                        if p not in waitlist:
                            queue.appendleft((p, visited))
                    visited += 1
            else:
                return -1

        return result


if __name__ == '__main__':
    cc = "keitgkggegyktyeytgyigkggktiigigkeyygtgytiygtkg"
    ee = [[0, 1], [1, 2], [2, 3], [1, 3], [3, 4], [4, 5], [5, 6], [3, 6], [5, 7], [6, 8], [5, 8], [7, 8], [8, 9],
          [7, 10], [8, 10], [9, 10], [10, 11], [9, 11], [7, 11], [5, 12], [11, 12], [11, 13], [13, 14], [12, 14],
          [12, 15], [10, 15], [14, 15], [7, 15], [9, 16], [13, 16], [12, 16], [15, 16], [11, 17], [14, 17], [16, 17],
          [15, 18], [14, 18], [17, 18], [18, 19], [14, 19], [13, 19], [14, 20], [15, 21], [12, 21], [20, 21], [19, 22],
          [20, 22], [21, 22], [22, 23], [19, 23], [11, 23], [18, 23], [13, 24], [23, 24], [21, 24], [24, 25], [13, 25],
          [23, 25], [15, 26], [23, 26], [25, 26], [24, 26], [26, 27], [25, 27], [26, 28], [27, 28], [20, 28], [23, 28],
          [11, 28], [23, 29], [29, 30], [25, 31], [26, 31], [15, 32], [30, 32], [31, 33], [27, 33], [30, 33], [28, 33],
          [29, 34], [32, 35], [33, 35], [34, 35], [35, 36], [13, 36], [34, 36], [30, 37], [36, 37], [35, 37], [24, 37],
          [35, 38], [34, 39], [37, 39], [37, 40], [39, 41], [37, 41], [41, 42], [38, 42], [40, 43], [43, 44], [39, 44],
          [35, 44], [38, 45], [44, 45], [26, 45]]
    s = Solution()
    print(s.largestPathValue(cc, ee))

left, mid, right = 0, 0, len(nums) - 1

while mid <= right:
    if nums[mid] == 0:
        nums[left], nums[mid] = nums[mid], nums[left]
        mid += 1
        left += 1
    elif nums[mid] == 1:
        mid += 1
    elif nums[mid] == 2:
        nums[right], nums[mid] = nums[mid], nums[right]
        right -= 1