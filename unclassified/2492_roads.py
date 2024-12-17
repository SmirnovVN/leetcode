from typing import List


def parent(graph, city):
    if graph[city][0] != city:
        return parent(graph, graph[city][0])
    return graph[city][0]


def union(graph, fst, snd):
    fst_p, snd_p = parent(graph, fst), parent(graph, snd)
    if fst_p == snd_p:
        return
    elif graph[fst_p][1] < graph[snd_p][1]:
        graph[fst_p][0] = snd_p
    elif graph[snd_p][1] < graph[fst_p][1]:
        graph[snd_p][0] = fst_p
    else:
        graph[snd_p][0] = fst_p
        graph[fst_p][1] += 1

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[i, 0] for i in range(n + 1)]
        result = float('inf')

        for road in roads:
            union(graph, road[0], road[1])

        fst_parent = parent(graph, 1)
        for road in roads:
            if fst_parent == parent(graph, road[0]):
                result = min(result, road[2])


        return result


if __name__ == '__main__':
    r = [[24, 31, 8660], [20, 67, 6537], [84, 4, 1105], [17, 87, 906], [38, 85, 924], [59, 46, 6195], [79, 3, 9974],
         [91, 44, 1089], [12, 76, 476], [76, 22, 5288], [70, 23, 8164], [6, 28, 574], [88, 91, 2182],
         [28, 49, 2214],
         [60, 21, 5998], [34, 82, 5693], [67, 35, 41], [4, 34, 2529], [47, 32, 6849], [1, 68, 3518], [78, 56, 1699],
         [40, 20, 8140], [37, 19, 2862], [87, 42, 7698], [68, 59, 6487], [86, 29, 6967], [9, 2, 8268],
         [30, 24, 8043],
         [89, 26, 424], [16, 15, 2522], [3, 33, 5776], [26, 25, 8333], [85, 39, 1811], [35, 75, 4313],
         [72, 12, 9124],
         [29, 37, 8787], [21, 47, 2395], [19, 89, 9288], [82, 88, 8766], [2, 50, 6239], [49, 92, 8292],
         [23, 6, 2149],
         [56, 86, 1185], [25, 16, 5914], [48, 84, 2640], [33, 5, 7728], [39, 48, 2096], [42, 9, 2364],
         [15, 72, 147],
         [50, 38, 3261], [31, 40, 5119], [32, 78, 6596], [22, 30, 3258], [5, 7, 2326], [7, 17, 2076], [75, 70, 819],
         [46, 79, 7631], [44, 60, 850]]
    s = Solution()
    print(s.minScore(92, r))
