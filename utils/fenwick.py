n = 1000
tree = [0] * (n + 1)


# from sortedcontainers import SortedList
def update(i, delta):
    while i <= n:
        tree[i] += delta
        i += i & -i


def query(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= i & -i
    return res

