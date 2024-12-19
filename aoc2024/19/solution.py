from math import inf


def count_possible(towels, patterns):
    result = 0

    for pattern in patterns:
        if count_combo(towels, pattern) > 0:
            result += 1

    return result


def sum_combo(towels, patterns):
    result = 0

    for pattern in patterns:
        result += count_combo(towels, pattern)

    return result


def count_combo(towels, pattern):
    n = len(pattern)
    dp = [0]*(n + 1)
    dp[0] = 1

    for i in range(n):
        for towel in towels:
            if i + len(towel) <= n and towel == pattern[i:i + len(towel)]:
                dp[i + len(towel)] += dp[i]

    return dp[-1]


def parse(data):
    towels = []
    patterns = []
    pattern = False
    for line in data:
        if line == '\n':
            pattern = True
        else:
            if pattern:
                patterns.append(line.strip())
            else:
                towels = line.strip().split(', ')

    return towels, patterns


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = count_possible(*test_1)
    print(res)
    assert res == 6

    res = count_possible(*inp)
    print(res)

    res = sum_combo(*test_1)
    print(res)
    assert res == 16

    res = sum_combo(*inp)
    print(res)
