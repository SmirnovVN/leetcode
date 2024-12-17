class Solution:
    def mincostTickets(self, days: [int], costs: [int]) -> int:
        spent = [0] * (days[-1] + 1)
        days = set(days)
        for i in range(1, len(spent)):
            if i in days:
                spent[i] = min(spent[max(i - 1, 0)] + costs[0], spent[max(i - 7, 0)] + costs[1],
                               spent[max(i - 30, 0)] + costs[2])
            else:
                spent[i] = spent[i - 1]
        return spent[-1]


if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    s = Solution()
    # print(s.mincostTickets(days, costs))
    # print(s.mincostTickets([1, 3, 7], [1, 4, 20]))
    print(s.mincostTickets([1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28], [3, 13, 45]))
