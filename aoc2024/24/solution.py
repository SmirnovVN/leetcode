from collections import defaultdict, deque

ops = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'XOR': lambda x, y: x ^ y
}


def apply_rules(regs, rules):
    q = deque(regs.keys())

    while q:
        first = q.popleft()
        for op, second, reg in rules[first]:
            if reg not in regs and second in regs:
                regs[reg] = ops[op](regs[first], regs[second])
                q.append(reg)

    return regs


def get_z(regs):
    result = 0
    cur = 0
    while f"z{cur:02d}" in regs:
        result += 2 ** cur * regs[f"z{cur:02d}"]
        cur += 1
    return result


def parse(data):
    regs = {}
    rules = defaultdict(list)
    upd = False
    for line in data:
        if line == '\n':
            upd = True
        else:
            if upd:
                s = line.strip().split(' ')
                rules[s[0]].append((s[1], s[2], s[4]))
                rules[s[2]].append((s[1], s[0], s[4]))
            else:
                s = line.split(': ')
                regs[s[0]] = int(s[1])

    return regs, rules


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = get_z(apply_rules(*test_1))
    print(res)
    assert res == 4

    res = get_z(apply_rules(*test_2))
    print(res)
    assert res == 2024

    res = get_z(apply_rules(*inp))
    print(res)
