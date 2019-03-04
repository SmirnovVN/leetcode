from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - n // 2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                    matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]


if __name__ == '__main__':
    s = Solution()

    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(m)
    assert m == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    m = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    s.rotate(m)
    assert m == [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]
