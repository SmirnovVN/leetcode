class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        if not k:
            return head

        n = 1
        cur = k_cur = head
        while cur.next:
            cur = cur.next
            n += 1

        k %= n
        for _ in range(n - k - 1):
            k_cur = k_cur.next

        cur.next = head
        head = k_cur.next
        k_cur.next = None

        return head


if __name__ == '__main__':
    if __name__ == '__main__':
        s = Solution()
        lst1 = ListNode(1)
        lst1.next = ListNode(2)
        lst1.next.next = ListNode(3)
        res = s.rotateRight(lst1, 2)
        assert res.val == 2
        assert res.next.val == 3
        assert res.next.next.val == 1
