from collections import deque, Counter


def sum_up(nums, k=2000):
    result = 0

    for num in nums:
        for i in range(k):
            num = evolve(num)

        result += num

    return result


def mix(num, secret):
    return num ^ secret


def prune(num):
    return num % 16777216


def evolve(secret):
    num = secret * 64
    num = mix(num, secret)
    secret = prune(num)
    num = secret // 32
    num = mix(num, secret)
    secret = prune(num)
    num = secret * 2048
    num = mix(num, secret)
    return prune(num)


def most_bananas(nums, k=2000):
    counters = []
    s = 0

    for num in nums:
        d = Counter()
        prev = evolve(num)
        q = deque()
        for i in range(k - 1):
            num = evolve(prev)
            q.append(num % 10 - prev % 10)
            if len(q) > 4:
                q.popleft()
            if len(q) == 4:
                t = tuple(q)
                if t not in d:
                    d[t] = num % 10
            prev = num

        s += num
        counters.append(d)

    result = Counter()
    for obj in counters:
        result.update(obj)

    mx = 0
    for k, v in result.items():
        if v > mx:
            mx = v

    return s, mx


def parse(data):
    result = []
    for line in data:
        result.append(int(line.strip()))

    return result


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('test_3.txt') as file:
        test_3 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = evolve(test_1[0])
    print(res)
    assert res == 15887950

    res = evolve(res)
    print(res)
    assert res == 16495136

    res = evolve(res)
    print(res)
    assert res == 527345

    res = evolve(res)
    print(res)
    assert res == 704524

    res = evolve(res)
    print(res)
    assert res == 1553684

    res = evolve(res)
    print(res)
    assert res == 12683156

    res = evolve(res)
    print(res)
    assert res == 11100544

    res = evolve(res)
    print(res)
    assert res == 12249484

    res = evolve(res)
    print(res)
    assert res == 7753432

    res = evolve(res)
    print(res)
    assert res == 5908254

    res = sum_up(test_2)
    print(res)
    assert res == 37327623

    res = most_bananas(test_1, k=10)
    print(res)
    assert res[1] == 6

    res = most_bananas(test_3)
    print(res)
    assert res[1] == 23

    res = most_bananas(inp)
    print(res)
