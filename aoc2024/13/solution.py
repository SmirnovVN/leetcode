import re
from math import inf


def min_tokens(a, b, prize):
    ax, ay = a
    bx, by = b
    px, py = prize
    result = inf
    x = y = ca = cb = 0
    while (x < px or y < py) and cb < 100:
        x, y = x + bx, y + by
        cb += 1

    while cb > 0 and ca < 100:
        if (x, y) == (px, py):
            result = min(result, ca * 3 + cb)
            ca += 1
        elif x < px or y < py:
            x, y = x + ax, y + ay
            ca += 1
        else:
            x, y = x - bx, y - by
            cb -= 1

    return result if result < inf else 0


def min_tokens2(a, b, prize):
    ax, ay = a
    bx, by = b
    px, py = prize
    b = (ax * py - ay * px) / (ax * by - ay * bx)
    a = (px - bx * b) / ax

    if a.is_integer() and b.is_integer():
        return int(a * 3 + b)
    return 0


def sum_up(machines):
    result = result2 = 0

    for a, b, prize in machines:
        result += min_tokens(a, b, prize)

    for a, b, prize in machines:
        result2 += min_tokens2(a, b, (10000000000000 + prize[0], 10000000000000 + prize[1]))

    return result, result2


def parse(file):
    result = []
    cur = []
    for line in file:
        extract = re.compile(r'\d+')
        numbers = extract.findall(line)
        if "Button A" in line:
            cur.append((int(numbers[0]), int(numbers[1])))
        elif "Button B" in line:
            cur.append((int(numbers[0]), int(numbers[1])))
        elif "Prize" in line:
            cur.append((int(numbers[0]), int(numbers[1])))
            result.append(cur)
            cur = []
    return result


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = sum_up(test_1)
    print(res)
    assert res[0] == 480

    # res = sum_up(test_2)
    # print(res)
    # assert res == 100161

    res = sum_up(inp)
    print(res)
    assert res[0] == 30973
