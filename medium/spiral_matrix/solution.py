from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n, m = len(matrix[0]), len(matrix)
        step = min(n, m)
        diff_n = n - step
        diff_m = m - step
        x, y = -1, 0
        result = []
        direction = 1
        while step > 0:
            for i in range(step + diff_n):
                x += direction
                result.append(matrix[y][x])
            step -= 1
            for i in range(step + diff_m):
                y += direction
                result.append(matrix[y][x])
            direction *= -1

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
