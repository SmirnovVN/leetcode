from collections import defaultdict


def find_sets(edges, length):
    prev = sets = set()
    graph = defaultdict(set)

    for i, o in edges:
        graph[i].add(o)
        graph[o].add(i)
        sets.add((i,))

    while length and sets:
        new_sets = set()
        for s in sets:
            candidates = graph[s[-1]]
            for c in candidates:
                connected = True
                for node in s:
                    if c not in graph[node]:
                        connected = False
                if connected:
                    new_sets.add(tuple(sorted(list(s) + [c])))
        length -= 1
        prev = sets
        sets = new_sets

    return prev


def cnt_correct(edges, correct):
    sets = find_sets(edges, 3)
    result = 0
    for s in sets:
        result += correct(s)

    return result


def starts_with_t(s):
    for c in s:
        if c[0] == 't':
            return 1

    return 0


def parse(data):
    result = []
    for line in data:
        result.append(line.strip().split('-'))
    return result


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = cnt_correct(test_1, starts_with_t)
    print(res)
    assert res == 7

    res = cnt_correct(inp, starts_with_t)
    print(res)

    res = find_sets(test_1, -1)
    res = ','.join(next(iter(res)))
    print(res)
    assert res == 'co,de,ka,ta'

    res = find_sets(inp, -1)
    print(','.join(next(iter(res))))
