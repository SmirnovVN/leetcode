class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1:
            result = l1
        else:
            return l2
        ten = 0
        last = l1
        while l1 and l2:
            l1.val += l2.val + ten
            if l1.val > 9:
                l1.val %= 10
                ten = 1
            else:
                ten = 0
            last = l1
            l1 = l1.next
            l2 = l2.next

        if l1:
            l1.val += ten
            ten = 0
            last = l1
        elif l2:
            l2.val += ten
            ten = 0
            last.next = l2
            last = l2

        if last.val > 9 or ten:
            last.val %= 10
            ten = 1
            while ten and last.next:
                last = last.next
                last.val += ten
                if last.val > 9:
                    last.val %= 10
                    ten = 1
                else:
                    ten = 0

            if ten:
                node = ListNode(1)
                last.next = node

        return result


if __name__ == '__main__':
    s = Solution()
    lst1 = ListNode(2)
    lst1.next = ListNode(4)
    lst1.next.next = ListNode(3)
    lst2 = ListNode(5)
    lst2.next = ListNode(6)
    lst2.next.next = ListNode(4)
    res = s.addTwoNumbers(lst1, lst2)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8
