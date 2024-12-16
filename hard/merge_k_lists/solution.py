from collections import deque
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(lst1, lst2):
    result = cur = None
    while lst1 and lst2:
        if lst1.val < lst2.val:
            if not result:
                result = cur = lst1
                lst1 = lst1.next
            else:
                cur.next = lst1
                cur = cur.next
                lst1 = lst1.next
        else:
            if not result:
                result = cur = lst2
                lst2 = lst2.next
            else:
                cur.next = lst2
                cur = cur.next
                lst2 = lst2.next

    if lst1:
        if not result:
            result = lst1
        else:
            cur.next = lst1

    if lst2:
        if not result:
            result = lst2
        else:
            cur.next = lst2

    return result


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = deque(lists)
        while True:
            first = queue.popleft()
            if queue:
                queue.append(merge(first, queue.popleft()))
            else:
                return first


if __name__ == '__main__':
    sol = Solution()
    lst1 = ListNode(2)
    lst1.next = ListNode(4)
    lst2 = ListNode(3)
    res = sol.mergeKLists([lst1, lst2])
    assert res.val == 2
    assert res.next.val == 3
    assert res.next.next.val == 4
