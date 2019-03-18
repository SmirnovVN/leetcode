class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            elif stack and brackets[bracket] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack


if __name__ == '__main__':
    sol = Solution()
    assert sol.isValid('()')
    assert sol.isValid('()[]{}')
    assert not sol.isValid('(]')
    assert not sol.isValid('([)]')
    assert sol.isValid('{[]}')
