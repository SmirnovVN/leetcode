from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            cycle_indexes = []
            cycle_size = n - 2 * i
            if cycle_size > 1:
                step = cycle_size - 1
                cycle_len = (step * 4)
                k = j = 0
                for j in range(i, i + cycle_size):
                    cycle_indexes.append((i, j))

                for k in range(i + 1, i + cycle_size):
                    cycle_indexes.append((k, j))

                for j in range(i + cycle_size - 2, i - 1, -1):
                    cycle_indexes.append((k, j))

                for k in range(i + cycle_size - 2, i, -1):
                    cycle_indexes.append((k, j))

                for c in range(step):
                    tmp = matrix[cycle_indexes[c][0]][cycle_indexes[c][1]]
                    for r in range(4):
                        to = cycle_indexes[(c + step * (r + 1)) % cycle_len]
                        matrix[to[0]][to[1]], tmp = tmp, matrix[to[0]][to[1]]


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
