
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cdirections = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def cost(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    def traverse(i, j, ch):
        area, perimeter = 0, 0
        if visited[i][j]:
            return area, perimeter
        visited[i][j] = 1
        area += 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == ch:
                na, np = traverse(ni, nj, ch)
                area, perimeter = area + na, perimeter + np
            else:
                perimeter += 1

        return area, perimeter

    result = 0
    for i in range(m):
        for j in range(n):
            area, perimeter = traverse(i, j, matrix[i][j])
            result += area * perimeter


    return result

def cost2(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    def traverse(i, j, ch):
        area, perimeter = 0, 0
        if visited[i][j]:
            return area, perimeter
        visited[i][j] = 1
        area += 1
        corner = False
        for di, dj in directions + [(0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == ch:
                na, np = traverse(ni, nj, ch)
                area, perimeter = area + na, perimeter + np
                corner = False
            else:
                perimeter += int(corner)
                corner = True
        for di, dj in cdirections:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] != ch:
                perimeter += int(matrix[i][nj] == ch and matrix[ni][j] == ch)

        return area, perimeter

    result = 0
    for i in range(m):
        for j in range(n):
            area, perimeter = traverse(i, j, matrix[i][j])
            result += area * perimeter


    return result



def parse(data):
    result = []
    for line in data:
        result.append(list(line.strip()))

    return result


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('test_3.txt') as file:
        test_3 = parse(file)
    with open('test_4.txt') as file:
        test_4 = parse(file)
    with open('test_5.txt') as file:
        test_5 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = cost(test_1)
    print(res)
    assert res == 140

    res = cost(test_2)
    print(res)
    assert res == 772

    res = cost(test_3)
    print(res)
    assert res == 1930

    res = cost(inp)
    print(res)

    res = cost2(test_1)
    print(res)
    assert res == 80

    res = cost2(test_2)
    print(res)
    assert res == 436

    res = cost2(test_4)
    print(res)
    assert res == 236

    res = cost2(test_5)
    print(res)
    assert res == 368

    res = cost2(inp)
    print(res)

