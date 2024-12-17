from operator import attrgetter
from bisect import bisect, bisect_left
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert = bisect(intervals, newInterval[0], key=lambda i: i[0])

        if insert == 0:
            if intervals[0][0] > newInterval[1]:
                return [newInterval] + intervals
        elif intervals[insert - 1][1] >= newInterval[0]:
            newInterval = [intervals[insert - 1][0], max(intervals[insert - 1][1], newInterval[1])]
            insert -= 1

        merge = bisect_left(intervals, newInterval[1], key=lambda i: i[1])
        if merge < len(intervals) and intervals[merge][0] <= newInterval[1]:
            newInterval[1] = max(intervals[merge][1], newInterval[1])
            merge += 1

        result = intervals[:insert] + [newInterval]

        if merge < len(intervals):
            result += intervals[merge:]

        return result


