from typing import List


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         result = []
#         while matrix:
#             rows, cols = len(matrix), len(matrix[0])
#             if rows > 1 and cols > 1:
#                 result += matrix[0] + [lst[-1] for lst in matrix[1::]]
#                 result += matrix[-1][-2::-1] + [lst[0] for lst in matrix[-2:0:-1]]
#                 matrix = [lst[1:-1:] for lst in matrix[1:-1:]]
#             elif rows == 1:
#                 result += matrix[0]
#                 break
#             elif cols == 1:
#                 result += [lst[0] for lst in matrix]
#                 break
#             else:
#                 break
#         return result

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x1, x2, y1, y2 = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result = []

        while x1 <= x2 and y1 <= y2:
            if y1 == y2:
                result += matrix[y1][x1:x2 + 1]
                break
            if x1 == x2:
                result += [i[x2] for i in matrix[y1:y2 + 1]]
                break
            result += matrix[y1][x1:x2 + 1]
            result += [i[x2] for i in matrix[y1 + 1:y2]]
            result += matrix[y2][x2:x1:-1]
            result += [i[x1] for i in matrix[y2:y1:-1]]
            x1 += 1
            x2 -= 1
            y1 += 1
            y2 -= 1

        return result


if __name__ == '__main__':

    # m = [[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]]
    m = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print(s.spiralOrder(m))

    m = [[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]]
    print(s.spiralOrder(m))

    m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(s.spiralOrder(m))

    m = [[1],[5],[9]]
    print(s.spiralOrder(m))
