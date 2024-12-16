from collections import defaultdict
from functools import cmp_to_key

directions = [(0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (1, 0)]


def sum_correct(order, updates, correct=False):
    result = 0

    rules = defaultdict(set)

    for i, o in order:
        rules[i].add(o)

    def compare(x, y):
        if y in rules[x]:
            return 1
        elif x in rules[y]:
            return -1
        else:
            return 0

    def is_correct(update):
        for i in range(len(update) - 1, -1, -1):
            if set(update[:i]).intersection(rules[update[i]]):
                return False
        return True

    for update in updates:
        c = is_correct(update)
        if c and not correct:
            result += update[len(update) // 2]
        elif not c and correct:
            update.sort(key=cmp_to_key(compare))
            result += update[len(update) // 2]



    return result


def parse(data):
    order = []
    updates = []
    upd = False
    for line in data:
        if line == '\n':
            upd = True
        else:
            if upd:
                s = line.split(',')
                updates.append(list(map(int, s)))
            else:
                s = line.split('|')
                order.append((int(s[0]), int(s[1])))

    return order, updates

if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = sum_correct(*test_1)
    print(res)
    assert res == 143

    res = sum_correct(*test_1, correct=True)
    print(res)
    assert res == 123

    res = sum_correct(*inp)
    print(res)

    res = sum_correct(*inp, correct=True)
    print(res)