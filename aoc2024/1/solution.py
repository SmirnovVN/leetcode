from collections import Counter


def sum_of_distances(first, second):
    first.sort()
    second.sort()
    result = 0
    for f, s in zip(first, second):
        result += abs(f - s)

    return result

def similarity(first, second):
    second = Counter(second)
    result = 0
    for f in first:
        result += second[f] * f

    return result


def parse(data):
    first, second = [], []
    for line in data:
        s = line.split('   ')
        first.append(int(s[0]))
        second.append(int(s[1]))

    return first, second

if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = sum_of_distances(test_1[0], test_1[1])
    print(res)
    assert res == 11

    res = sum_of_distances(test_2[0], test_2[1])
    print(res)
    assert res == 15

    res = sum_of_distances(inp[0], inp[1])
    print(res)

    res = similarity(test_1[0], test_1[1])
    print(res)
    assert res == 31

    res = similarity(test_2[0], test_2[1])
    print(res)
    assert res == 6

    res = similarity(inp[0], inp[1])
    print(res)