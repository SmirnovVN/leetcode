def denominators(n):
    res = set()

    if n > 0:
        for i in range(2, int(n ** .5) + 1):
            while n % i == 0:
                res.add(i)
                n //= i

        if n > 1:
            res.add(n)

    return res
