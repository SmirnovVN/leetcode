class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next


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
