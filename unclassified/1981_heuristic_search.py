from heapq import heappop, heappush


def min_possible_distance(target, min_remnant, max_remnant):
    if min_remnant <= target <= max_remnant:
        return 0
    else:
        return min_remnant - target if target < min_remnant else target - max_remnant


class Solution:
    def minimizeTheDifference(self, mat, target):
        m, n = len(mat), len(mat[0])
        set_mat = [set(row) for row in mat]
        mins = [min(row) for row in set_mat]
        maxs = [max(row) for row in set_mat]
        cum_min, cum_max = 0, 0
        min_remnants, max_remnants = [0], [0]
        for i in range(m):
            cum_min += mins[i]
            min_remnants.append(cum_min)
            cum_max += maxs[i]
            max_remnants.append(cum_max)

        min_distance = max(min_possible_distance(target, min_remnants[m], max_remnants[m]), target)
        unchecked = [(min_distance, m, target)]
        checked = set()
        while unchecked:
            mpd, row, distance = heappop(unchecked)
            checked.add((mpd, row, distance))
            if row > 0:
                row -= 1
                for i in set_mat[row]:
                    mpd = min_possible_distance(distance - i, min_remnants[row], max_remnants[row])
                    if mpd <= min_distance and (mpd, row, distance - i) not in checked:
                        heappush(
                            unchecked,
                            (mpd, row, distance - i)
                        )
            else:
                if min_distance > abs(distance):
                    if distance == 0:
                        return 0
                    min_distance = abs(distance)
                    new_unchecked = [(mpd, row, distance)
                                     for (mpd, row, distance) in unchecked
                                     if mpd <= min_distance]
                    unchecked = []
                    for value in new_unchecked:
                        heappush(unchecked, value)

        return min_distance

if __name__ == '__main__':
    s = Solution()
    mt = [[10,3,7,7,9,6,9,8,9,5],[1,1,6,8,6,7,7,9,3,9],[3,4,4,1,3,6,3,3,9,9],[6,9,9,3,8,7,9,6,10,6]]
    print(s.minimizeTheDifference(mt, 5))
    mt = [[24,18,31,34,31,47,47,27,32,44,19,26,15,11,32,39,17,36,28,45,44,45,6,38,47,37,7,5,23,12,35,10,27,5,6,44,42,3,9],[19,25,15,46,43,44,22,29,12,34,19,8,10,35,49,28,7,22,34,16,46,33,17,11,11,30,46,16,26,23,49,37,47,10,30,29,47,2,39],[25,48,12,26,33,4,31,18,26,17,46,47,27,46,42,31,24,36,22,46,48,43,6,49,47,15,35,40,13,26,43,25,41,1,21,30,34,46,30],[42,12,7,2,26,14,47,37,39,25,14,7,25,36,50,13,18,48,38,38,13,32,40,9,1,40,44,28,31,17,33,37,12,30,46,14,49,5,23],[1,32,35,43,43,5,49,38,32,44,22,30,18,33,30,2,6,40,49,23,12,49,49,26,17,44,41,47,9,4,11,32,25,30,44,19,10,1,19],[36,30,1,24,3,35,25,37,29,14,44,20,32,42,9,31,45,35,46,20,5,17,21,20,22,42,20,42,42,26,34,6,33,41,14,26,39,34,10],[33,41,6,20,3,15,30,36,15,34,18,4,8,8,44,25,24,14,21,23,5,22,30,24,11,32,29,19,30,9,46,29,41,14,18,21,11,7,16],[31,13,49,44,24,12,23,9,9,15,18,36,41,25,26,48,22,18,47,39,33,38,45,47,21,48,26,49,46,46,41,49,46,19,35,40,41,43,5],[24,20,26,31,12,17,23,29,31,6,12,21,25,9,2,7,23,11,23,5,47,49,42,28,1,35,21,16,39,25,35,19,31,41,10,24,21,13,32],[7,10,14,22,17,10,27,24,17,6,22,13,16,46,16,47,40,3,22,24,42,50,40,4,10,12,5,28,29,50,18,9,21,34,37,8,22,42,50],[46,40,26,15,4,26,50,31,32,40,21,35,40,39,6,38,33,35,43,32,26,45,30,11,27,25,34,29,3,7,29,38,9,8,44,33,12,5,26],[20,30,46,1,17,7,43,23,15,12,2,10,28,43,6,22,42,30,4,31,16,5,31,9,36,2,9,45,33,35,4,4,13,35,1,34,22,44,34],[16,9,24,32,1,9,35,8,16,7,30,14,4,40,14,41,25,22,40,42,26,46,34,33,50,44,11,33,7,10,41,14,12,25,13,20,22,28,10],[28,9,26,21,20,7,36,7,31,18,19,34,49,32,18,15,27,45,9,45,36,43,7,2,39,36,49,13,14,13,26,38,3,42,9,41,2,48,17],[45,47,31,35,4,48,50,15,10,39,21,3,45,13,7,9,41,45,35,12,49,6,44,30,41,19,14,11,21,45,18,34,37,5,27,27,43,47,3],[30,20,43,8,41,45,47,18,2,14,27,22,17,35,47,26,38,34,48,13,28,50,9,45,11,29,30,23,25,31,40,17,40,13,38,31,29,13,49],[31,37,22,20,5,11,24,39,41,31,15,50,40,42,43,37,9,44,20,14,35,20,7,1,2,13,21,4,21,35,17,47,43,22,29,5,27,31,46],[2,19,38,37,9,14,10,11,39,50,25,47,5,41,38,29,18,42,6,32,31,16,10,37,20,15,13,40,46,22,38,40,45,26,34,27,16,42,14],[36,4,17,43,16,9,40,47,26,28,8,30,26,26,31,25,19,14,16,15,4,35,34,6,39,35,44,1,4,25,46,28,26,15,33,18,7,24,33],[24,34,32,38,5,46,30,48,45,15,18,2,2,31,3,9,42,10,14,21,16,35,4,40,10,42,19,49,7,42,36,35,6,44,43,9,28,46,9],[3,20,33,43,18,31,4,36,23,49,22,44,7,39,24,7,39,23,24,41,18,31,19,33,39,10,2,3,22,28,41,1,23,44,35,46,4,43,5],[45,35,33,40,50,28,28,27,16,12,11,40,3,2,38,49,47,23,44,12,19,2,3,16,37,15,26,5,24,8,39,5,16,15,36,13,7,1,45],[26,6,33,18,38,42,15,4,34,34,34,26,28,9,10,28,9,30,48,24,4,37,12,34,29,28,39,42,29,11,32,39,9,23,10,2,17,46,12],[10,41,27,37,41,17,29,31,30,13,28,28,18,50,15,23,49,41,3,26,40,2,28,20,2,36,31,37,17,44,18,16,30,46,30,24,34,40,30],[43,16,36,35,11,30,19,49,24,27,8,33,44,16,48,42,43,25,8,28,39,30,40,34,30,6,48,25,29,40,50,46,45,48,24,36,23,11,10],[15,43,42,12,27,29,32,46,47,12,27,17,21,37,26,20,42,46,17,43,21,43,1,26,38,3,14,30,7,8,1,24,21,39,21,47,26,12,48],[21,6,34,39,31,26,40,16,29,7,39,2,23,2,20,32,9,46,46,4,1,22,26,31,42,40,1,31,41,37,14,15,48,40,21,11,22,20,50],[26,37,39,47,32,30,49,18,6,33,14,37,24,16,24,24,12,16,35,42,47,40,15,14,38,30,16,26,18,38,14,33,11,1,26,50,31,48,24],[42,12,44,13,47,45,39,12,32,40,1,47,9,14,46,14,1,40,6,30,50,41,13,48,12,18,26,40,2,1,24,8,20,3,37,24,31,25,8],[5,30,12,10,50,30,42,5,18,10,31,35,5,34,46,19,19,2,36,36,14,5,27,9,12,38,20,30,13,3,45,22,30,4,10,15,40,23,41],[20,45,42,7,13,10,15,2,21,8,18,7,24,50,5,33,46,40,9,23,9,28,47,48,13,20,36,49,2,49,2,22,41,10,47,5,35,49,4],[9,48,32,27,44,23,31,43,19,20,5,41,10,48,8,1,6,10,23,46,10,20,50,37,44,35,9,6,15,37,47,50,48,15,22,6,12,43,28]]
    print(s.minimizeTheDifference(mt, 145))
    mt = [[34,27,41,28,39,21,10,42,26,50,32,7,34,22,15,48,35,9,39,17,41,2,26,13,7,21,39,10,50,3,14,15,29,15,49,13,18,20],[3,1,49,50,16,14,32,25,27,30,16,41,33,44,44,3,39,10,47,4,22,47,33,11,18,40,45,9,24,30,21,34,22,41,33,29,49,23],[12,23,20,24,38,26,47,8,1,40,14,4,35,3,11,26,34,14,34,28,18,23,32,26,13,25,25,20,49,37,2,50,23,10,16,42,28,10],[12,48,33,10,39,36,32,19,41,1,41,23,13,45,31,44,49,42,37,4,25,35,34,33,36,29,37,9,20,15,20,35,20,3,13,4,13,8],[3,40,41,6,1,23,16,47,17,27,43,20,5,29,47,47,34,14,9,5,47,43,40,14,35,8,11,18,10,25,30,22,45,39,26,34,22,48],[29,10,45,34,3,36,21,13,2,9,42,23,4,45,4,20,4,3,47,32,36,39,28,11,8,38,3,32,20,3,34,39,24,1,11,9,47,1],[41,49,45,30,19,23,41,34,12,5,42,42,44,1,3,15,7,23,25,24,25,24,5,6,41,37,26,11,9,10,37,43,19,44,10,4,9,17],[42,24,27,21,23,28,34,25,27,48,48,25,23,39,8,15,6,34,1,15,36,9,5,50,45,12,2,4,35,22,17,44,44,14,6,7,29,7],[13,47,23,24,14,3,21,16,38,22,34,46,41,23,42,1,33,33,22,39,1,37,34,33,8,2,41,13,33,3,45,15,47,27,8,14,36,37],[48,12,33,46,3,24,7,35,37,32,10,36,19,35,3,48,15,1,19,33,14,12,22,28,18,25,39,12,10,39,43,8,4,46,2,48,5,18],[23,20,10,47,27,14,25,15,15,17,20,27,24,37,16,48,21,34,42,41,17,8,50,18,21,20,47,32,11,18,18,49,29,23,21,39,10,23],[28,12,5,11,5,45,50,16,21,6,11,19,8,27,9,18,39,19,3,5,17,19,26,26,7,7,30,35,11,50,36,1,4,40,9,21,46,16],[4,36,32,5,5,6,31,35,38,40,35,35,25,43,14,38,1,22,37,22,38,25,15,22,15,4,5,4,39,8,20,8,14,21,14,4,25,22],[5,35,33,28,45,18,8,7,22,9,20,43,22,18,10,29,32,22,25,31,24,42,29,21,28,43,30,46,40,34,36,48,22,40,24,19,32,48],[24,11,21,22,27,9,1,17,21,7,19,35,26,19,7,41,7,7,15,27,41,15,37,4,34,40,2,29,44,44,16,46,4,10,35,31,32,9],[21,18,27,31,24,39,16,27,22,3,5,42,32,7,20,34,49,9,10,40,20,38,22,28,18,9,39,37,29,35,17,48,26,7,4,38,14,15],[41,14,48,4,39,23,40,6,21,24,34,49,42,25,44,27,45,6,39,37,48,3,17,19,1,14,42,26,20,14,23,8,28,39,20,5,16,29],[23,36,34,48,30,12,38,2,38,23,45,31,22,30,31,27,36,40,29,8,3,25,28,50,13,28,8,31,35,28,37,24,15,12,24,35,37,34],[33,11,12,46,50,9,42,37,30,12,22,9,26,15,45,44,13,50,22,48,30,17,17,1,37,33,28,32,13,22,30,28,1,43,6,20,18,7],[42,49,48,19,23,31,24,7,29,3,21,39,49,27,50,22,24,32,30,1,35,35,29,1,33,22,45,25,41,8,50,2,27,29,2,24,26,46],[44,46,44,22,14,12,8,18,42,31,40,48,3,26,38,4,32,40,49,41,36,43,12,5,21,4,41,33,46,38,45,7,17,33,33,4,48,22],[33,8,34,10,14,28,5,22,48,35,6,32,35,19,47,10,42,26,3,7,22,21,41,30,11,50,47,40,44,4,47,16,46,43,7,10,26,16],[3,33,49,41,44,2,24,41,19,22,22,25,49,47,15,38,6,26,18,17,32,28,8,48,22,37,20,36,11,39,41,44,29,44,33,42,19,14],[22,8,14,49,30,16,17,9,33,4,22,4,17,9,48,33,13,39,28,24,9,48,46,2,31,20,12,23,7,21,16,42,22,48,26,41,16,26],[4,4,19,18,38,13,35,32,46,41,29,28,50,1,1,28,10,18,37,48,12,23,28,39,25,2,48,41,30,12,19,42,38,42,2,44,16,48],[24,25,23,18,19,22,5,27,43,29,49,49,47,28,31,7,18,22,49,7,30,22,28,5,12,24,14,10,26,39,36,26,31,6,16,21,6,35],[35,44,1,41,4,30,40,8,14,34,35,38,5,31,31,24,28,23,33,34,8,5,41,30,42,33,18,24,37,30,48,17,16,29,23,27,16,19],[7,1,39,49,38,40,12,9,30,42,35,17,5,12,17,31,7,30,11,31,10,26,48,6,28,44,43,16,31,48,36,45,35,28,10,12,42,28],[38,34,50,1,43,34,47,44,35,49,32,3,21,50,2,33,35,35,48,1,30,13,32,28,17,16,3,45,33,15,33,27,47,31,14,39,9,8],[35,19,21,10,3,36,48,17,12,5,30,20,31,28,9,22,12,34,11,26,17,7,37,12,23,40,40,23,7,19,38,31,22,40,39,41,22,42],[49,5,20,2,10,8,35,43,16,18,7,45,17,48,7,10,41,49,47,32,47,13,41,8,41,6,8,13,8,22,26,22,6,26,17,13,45,8],[8,16,44,45,46,37,4,2,14,50,8,23,30,32,48,36,3,4,50,44,19,20,4,28,6,12,14,35,24,2,48,39,33,9,36,10,13,38],[41,11,9,7,39,45,11,46,15,38,49,20,36,10,22,20,12,12,24,44,24,39,1,22,23,18,48,17,15,24,11,9,5,20,28,44,1,25],[1,40,24,5,4,33,35,27,50,32,14,2,27,7,30,49,39,29,23,43,45,20,9,49,31,30,43,37,15,27,48,49,33,12,16,31,22,6],[35,21,42,9,39,29,25,23,29,48,4,1,42,15,24,6,31,48,31,16,6,33,10,9,50,35,29,33,13,28,12,18,11,14,25,2,46,22],[36,25,45,42,3,8,19,33,19,19,28,19,4,1,1,6,27,9,5,36,14,30,4,25,39,2,2,41,46,25,8,12,28,24,25,20,13,49],[9,32,43,15,49,3,31,9,16,12,14,40,31,38,32,31,9,5,6,26,17,25,15,35,1,27,40,41,50,14,28,29,20,12,19,26,5,43],[45,28,41,6,25,41,44,49,12,24,24,26,49,18,24,30,8,50,45,11,41,27,43,17,47,22,2,13,43,5,20,46,30,49,23,8,29,24],[48,27,47,27,13,34,44,40,40,41,35,42,38,48,11,37,17,23,37,12,18,9,4,5,41,44,14,7,35,3,32,28,40,15,33,21,38,35],[34,8,26,41,33,17,11,50,50,15,1,12,45,39,26,32,7,6,4,15,23,8,42,8,22,27,3,44,20,26,41,30,12,33,42,26,20,36],[46,13,17,4,7,37,41,44,1,16,18,6,28,49,29,8,24,16,41,23,17,49,5,25,46,2,46,11,49,8,17,47,27,13,30,2,25,9],[35,36,38,8,5,2,35,43,45,20,34,3,40,6,20,6,29,47,7,23,25,40,2,37,30,10,44,35,14,35,31,8,40,21,4,19,14,1],[17,30,44,10,31,35,6,21,5,48,42,15,8,24,15,7,21,46,8,1,8,33,40,37,33,10,22,36,9,33,5,4,13,32,13,9,44,49],[16,32,28,42,21,12,16,2,12,29,20,46,26,32,22,13,27,5,46,20,28,23,30,17,13,28,13,4,50,9,2,41,18,19,25,31,12,47],[44,11,48,11,7,17,4,10,46,50,20,30,44,21,5,19,36,49,21,42,25,36,4,3,26,28,20,45,41,49,15,21,29,4,38,44,3,30]]
    print(s.minimizeTheDifference(mt, 20))
    mt = [[70,1,1,1,70,1,70,70,70,3,1,1,1,1,70,70,1,70,1,70,70,70,70,1,70,70,1,70,1,1,70,1,70,1,70,70,70],[1,1,1,70,1,70,70,1,70,70,70,70,1,70,70,70,70,1,70,1,70,1,70,1,1,1,3,1,1,70,1,1,70,70,70,1,70],[70,1,1,1,70,70,70,1,1,3,1,1,1,70,1,1,70,1,1,70,1,70,70,70,1,1,1,70,70,70,1,70,70,70,1,1,70],[70,1,1,70,70,70,1,1,1,1,70,1,70,70,1,70,1,70,3,1,70,70,1,1,70,70,70,1,1,70,70,1,70,70,1,70,1],[1,1,70,1,70,1,1,70,70,1,70,70,70,1,70,1,70,1,1,70,70,1,1,70,1,1,1,70,70,1,70,1,1,3,70,70,70],[70,70,70,70,1,1,1,70,70,1,70,70,1,70,70,1,1,1,70,1,70,70,1,70,70,70,70,1,1,70,70,70,1,70,3,70,70],[1,1,70,1,1,70,1,1,70,1,1,70,70,1,70,1,1,70,1,1,70,1,70,70,1,1,1,1,3,70,70,1,1,70,70,70,1],[1,70,1,1,70,70,70,70,1,70,1,70,1,70,70,1,1,1,70,70,70,1,1,70,1,70,1,70,1,1,70,70,70,1,3,1,70],[1,1,1,1,1,1,70,70,1,1,1,1,1,70,70,1,70,70,70,1,70,1,1,1,70,1,1,70,1,70,70,70,3,1,70,70,1],[1,1,70,1,70,70,3,1,70,70,1,1,70,1,1,1,1,70,70,70,1,70,70,70,1,70,70,1,1,1,70,70,1,1,70,1,1],[70,70,70,1,1,1,70,1,70,70,1,70,70,70,1,1,1,1,1,1,1,1,70,70,1,1,70,1,1,3,70,70,1,70,70,1,1],[1,1,70,1,1,70,1,70,3,70,1,1,1,1,70,1,70,1,70,70,70,70,70,1,1,1,1,70,70,70,1,70,70,70,1,70,1],[70,70,70,1,70,1,1,1,70,70,1,70,70,1,1,70,1,3,70,1,70,1,70,1,1,70,1,70,1,1,1,70,1,1,70,1,1],[70,1,70,1,1,70,70,70,70,70,70,70,1,70,1,1,1,70,1,1,70,70,70,70,1,1,70,70,70,3,70,70,1,70,70,70,1],[70,1,70,1,3,70,70,70,70,70,1,70,1,1,1,1,1,1,1,1,70,70,70,70,70,70,1,70,1,70,70,1,70,1,70,1,1],[1,1,70,1,1,70,1,1,3,1,1,1,1,1,70,1,70,70,1,70,1,70,1,1,1,70,1,70,70,70,70,70,1,70,1,1,1],[3,1,1,70,70,70,1,1,70,70,70,70,1,1,70,1,70,1,70,70,70,1,70,1,70,1,1,70,70,70,70,70,70,70,1,1,70],[70,1,70,1,70,1,1,1,1,1,1,1,70,70,70,70,1,1,70,1,70,70,1,70,70,70,1,70,1,1,1,1,1,70,3,70,70],[1,3,70,1,70,70,1,70,1,70,1,1,1,1,1,70,70,70,70,70,1,1,70,70,70,1,70,70,70,70,70,70,70,1,1,70,70],[70,1,1,1,1,70,1,70,70,1,3,1,1,1,70,1,1,1,1,1,1,1,70,1,1,70,70,70,1,70,1,1,70,70,1,1,1],[70,70,1,1,70,1,70,70,70,70,70,70,70,70,1,1,3,1,1,1,1,1,1,1,1,70,70,1,1,1,1,70,1,1,70,70,70],[1,1,70,70,70,70,70,1,1,1,70,1,3,70,70,70,1,1,70,1,1,1,1,70,70,70,70,70,70,1,70,1,1,1,1,70,1],[1,1,70,70,1,1,3,1,1,1,70,1,1,1,70,70,70,1,70,70,1,70,70,1,1,70,1,70,1,70,1,1,1,70,70,70,1],[1,1,1,1,70,70,1,70,1,70,1,70,70,1,70,70,1,1,70,1,70,1,1,1,1,70,70,70,70,1,70,3,70,70,70,1,70],[1,1,70,1,1,1,70,1,1,70,1,1,70,1,1,70,1,1,1,1,70,1,1,1,3,1,70,70,70,1,70,70,1,1,1,70,1],[1,1,1,70,1,1,1,70,70,70,1,1,70,70,1,70,70,1,1,1,70,70,70,1,1,70,70,70,1,1,70,1,70,1,70,1,3],[70,1,1,1,70,1,1,1,1,1,70,1,70,1,1,1,70,1,70,1,3,1,1,70,1,1,1,1,70,70,1,1,70,70,70,1,1],[70,1,1,1,1,70,70,70,1,70,1,1,1,1,1,1,70,1,3,70,1,1,70,70,70,70,1,1,1,70,1,1,70,1,70,70,70],[70,70,1,1,1,1,1,1,70,1,70,1,1,1,70,70,70,70,1,1,1,1,1,1,70,1,1,70,1,1,70,70,70,1,70,3,70],[1,70,1,1,70,70,1,70,1,70,70,1,70,1,1,1,3,70,70,70,70,70,70,1,1,1,70,1,70,1,70,1,70,1,70,1,1],[70,1,70,70,1,1,70,70,1,1,70,70,1,1,70,1,1,70,1,70,1,1,70,1,1,1,70,70,1,70,1,70,1,70,1,70,3],[70,1,70,1,1,70,1,1,1,1,1,1,70,70,1,70,70,70,70,70,3,1,1,70,70,70,1,1,70,1,1,1,1,70,1,1,70],[1,70,70,70,1,70,1,70,1,1,70,1,70,1,70,1,1,1,1,1,1,1,1,70,70,1,70,1,70,70,1,1,70,70,3,70,70],[70,3,70,70,1,1,1,70,1,1,70,70,1,1,1,70,70,70,1,1,70,1,1,70,1,70,70,1,1,1,70,1,70,1,1,1,70],[70,70,1,1,1,70,1,70,1,1,70,70,1,70,70,70,1,70,1,70,1,70,1,70,1,70,70,1,1,70,1,70,1,1,1,3,70],[70,1,70,1,1,70,1,1,1,1,1,1,70,70,1,1,70,70,1,70,70,1,70,70,1,1,70,1,1,3,70,70,70,1,1,70,1],[1,70,1,1,1,70,1,1,70,1,70,70,70,1,1,70,1,1,3,1,70,1,70,70,1,1,1,1,1,1,70,1,1,1,1,70,1]]
    print(s.minimizeTheDifference(mt, 113))
