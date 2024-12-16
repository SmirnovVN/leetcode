directions = [(0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (1, 0)]



def count(text, search='XMAS'):
    m, n = len(text), len(text[0])
    result = 0
    for i in range(m):
        for j in range(n):
            if text[i][j] == search[0]:
                for si, sj in directions:
                    x, y = i + si, j + sj
                    for k in range(1, len(search)):
                        if 0 <= x < m and 0 <= y < n and text[x][y] == search[k]:
                            x += si
                            y += sj
                        else:
                            break
                    else:
                        result += 1

    return result


def count2(text):
    m, n = len(text), len(text[0])

    def seacrh(i, j, search, direction):
        for k in range(len(search)):
            if 0 <= i < m and 0 <= j < n and text[i][j] == search[k]:
                i, j = i + direction[0], j + direction[1]
            else:
                return False
        return True

    def xmas(i, j):
        searches = ['MAS', 'SAM']
        result = 0
        for search in searches:
            for bias, direction in [(0, (1, 1)), (2, (1, -1))]:
                if seacrh(i, j + bias, search, direction):
                    result += 1

        return result == 2



    result = 0
    for i in range(m):
        for j in range(n):
            if xmas(i, j):
                result += 1

    return result


def parse(data):
    result = []
    for line in data:
        result.append(line)

    return result

if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = count(test_1), count2(test_1)
    print(res)
    assert res == (4, 0)

    res = count(test_2), count2(test_2)
    print(res)
    assert res == (18, 9)

    res = count(inp), count2(inp)
    print(res)