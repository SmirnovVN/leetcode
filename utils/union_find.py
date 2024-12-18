class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            return self.find(self.parent[node])
        return node

    def union(self, fst, snd):
        fst_p, snd_p = self.find(fst), self.find(snd)

        if fst_p == snd_p:
            return
        if self.rank[fst_p] > self.rank[snd_p]:
            fst_p, snd_p = snd_p, fst_p
        self.rank[snd_p] += self.rank[fst_p]
        self.parent[fst_p] = snd_p


class UnionFind:
    def __init__(self, m, n):
        self.parent = [[None]*n for _ in range(m)]
        self.rank = [[1]*n for _ in range(m)]

    def find(self, node):
        i, j = node
        if self.parent[i][j]:
            return self.find(self.parent[i][j])
        return node

    def union(self, fst, snd):
        (fi, fj), (si, sj) = self.find(fst), self.find(snd)

        if (fi, fj) == (si, sj):
            return
        if self.rank[fi][fj] > self.rank[si][sj]:
            (fi, fj), (si, sj) = (si, sj), (fi, fj)
        self.rank[si][sj] += self.rank[fi][fj]
        self.parent[fi][fj] = (si, sj)