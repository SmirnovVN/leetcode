from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result, prev_val = inf, -inf
        q = [TreeNode(-inf, None, root)]
        while q and result > 1:
            cur = q.pop()
            result, prev_val = min(result, cur.val - prev_val), cur.val
            cur = cur.right
            while cur:
                q.append(cur)
                cur = cur.left

        return result
