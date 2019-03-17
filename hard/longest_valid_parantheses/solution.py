class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        cur = 0
        n = len(s)
        stack = [-1]
        while cur < n:
            if s[cur] == '(':
                stack.append(cur)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, cur - stack[-1])
                else:
                    stack.append(cur)
            cur += 1

        return max_len


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestValidParentheses('(()') == 2
    assert sol.longestValidParentheses(')()())') == 4
