from bisect import bisect_right


def lis(a):
    n = len(a)
    d = [float('Inf')]*(n+1)
    d[0] = -float('Inf')
    p = [-1] * (n+1)
    r = [-1] * (n+1)
    for i in range(n):
        j = bisect_right(d, a[i])
        if d[j - 1] <= a[i] <= d[j]:
            d[j] = a[i]
            p[j] = i
            r[i] = p[j-1]
    j = 1
    while j < n + 1 and p[j] != -1:
        j += 1
    j -= 1
    i = p[j]
    res = [-1]*j
    while j > 0:
        res[j-1] = i
        j -= 1
        i = r[i]
    return res


def main():
    a = [5, 3, 4, 4, 2, 5, 9]
    a.reverse()
    res = lis(a)
    res.reverse()
    print(len(res))
    print(" ".join(map(str, map(lambda x: len(a) - x, res))))


if __name__ == "__main__":
    main()
