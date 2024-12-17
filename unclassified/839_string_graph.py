class Graph:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def parent(self, node):
        if self.parents[node] != node:
            return self.parent(self.parents[node])
        return node

    def union(self, fst, snd):
        fst_p, snd_p = self.parent(fst), self.parent(snd)

        if fst_p == snd_p:
            return
        elif self.ranks[fst_p] < self.ranks[snd_p]:
            self.parents[fst_p] = self.parents[snd_p]
        elif self.ranks[snd_p] < self.ranks[fst_p]:
            self.parents[snd_p] = self.parents[fst_p]
        else:
            self.parents[snd_p] = self.parents[fst_p]
            self.ranks[fst_p] += 1


class Solution:
    def numSimilarGroups(self, strs: [str]) -> int:
        n, ln = len(strs), len(strs[0])

        g = Graph(n)

        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                for k in range(ln):
                    if strs[i][k] != strs[j][k]:
                        if diff == 2 or strs[j][strs[j].find(strs[i][k])] != strs[i][k]:
                            break
                        diff += 1
                else:
                    g.union(i, j)

        result = set()
        for i in range(n):
            result.add(g.parent(i))

        return len(result)


if __name__ == '__main__':
    s = Solution()
    c = ["jmijc","imjjc","jcijm","cmijj","mijjc"]
    print(s.numSimilarGroups(c))
    assert s.numSimilarGroups(c) == 1
