
directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}

def move(matrix, moves):
    matrix = [[cell for cell in row] for row in matrix]
    m, n = len(matrix), len(matrix[0])
    x, y = 1, 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '@':
                x, y = j, i
                matrix[i][j] = '.'

    for m in moves:
        nx, ny = x + directions[m][1], y + directions[m][0]
        if matrix[ny][nx] == '#':
            continue
        elif matrix[ny][nx] == 'O':
            ex, ey = nx + directions[m][1], ny + directions[m][0]
            while matrix[ey][ex] == 'O':
                ex, ey = ex + directions[m][1], ey + directions[m][0]
            if matrix[ey][ex] == '.':
                matrix[ey][ex], matrix[ny][nx] = matrix[ny][nx], matrix[ey][ex]
            elif matrix[ey][ex] == '#':
                continue

        x, y = nx, ny


    return matrix

def move2(matrix, moves):
    m, n = len(matrix), len(matrix[0])
    new_matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            if matrix[i][j] == '@':
                row += ['@', '.']
            if matrix[i][j] == '#':
                row += ['#', '#']
            if matrix[i][j] == '.':
                row += ['.', '.']
            if matrix[i][j] == 'O':
                row += ['[', ']']
        new_matrix.append(row)

    matrix = new_matrix

    n = len(matrix[0])
    x, y = 1, 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '@':
                x, y = j, i
                matrix[i][j] = '.'

    for m in moves:
        # print(m, x, y)
        # print('\n'.join(''.join(row) for row in matrix))
        nx, ny = x + directions[m][1], y + directions[m][0]
        if matrix[ny][nx] == '#':
            continue
        elif matrix[ny][nx] in {'[', ']'}:
            q = [(nx, ny)]
            affected = [(nx, ny)]
            if directions[m][0]:
                if matrix[ny][nx] == '[':
                    q.append((nx + 1, ny))
                    affected.append((nx + 1, ny))
                else:
                    q.append((nx - 1, ny))
                    affected.append((nx - 1, ny))
            checked = set()
            stop = False
            while q and not stop:
                new_q = []
                for qx, qy in q:
                    if (qx, qy) in checked:
                        continue
                    checked.add((qx, qy))
                    ex, ey = qx + directions[m][1], qy + directions[m][0]
                    if (ex, ey) in new_q:
                        continue
                    if matrix[ey][ex] == '#':
                        stop = True
                        break
                    if matrix[ey][ex] in {'[', ']'}:
                        new_q.append((ex, ey))
                        affected.append((ex, ey))
                        if directions[m][0]:
                            if matrix[ey][ex] == '[' and (ex + 1, ey) not in new_q:
                                new_q.append((ex + 1, ey))
                                affected.append((ex + 1, ey))
                            elif (ex - 1, ey) not in new_q:
                                new_q.append((ex - 1, ey))
                                affected.append((ex - 1, ey))
                q = new_q
            if stop:
                continue
            else:
                for ex, ey in affected[::-1]:
                    ax, ay = ex + directions[m][1], ey + directions[m][0]
                    matrix[ey][ex], matrix[ay][ax] = matrix[ay][ax], matrix[ey][ex]

        x, y = nx, ny


    return matrix


def get_gps(matrix):
    m, n = len(matrix), len(matrix[0])
    result = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] in {'O', '['}:
                result += i * 100 + j

    return result


def parse(file):
    result = []
    moves = False
    m = []
    for line in file:
        if line == '\n':
            moves = True
        if moves:
            m += list(line.strip())
        else:
            result.append(list(line.strip()))
    return result, m



if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('test_3.txt') as file:
        test_3 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = get_gps(move(*test_1))
    print(res)
    assert res == 2028

    res = get_gps(move(*test_2))
    print(res)
    assert res == 10092

    res = get_gps(move2(*test_3))
    print(res)

    res = get_gps(move2(*test_2))
    print(res)
    assert res == 9021

    res = get_gps(move(*inp))
    print(res)

    res = get_gps(move2(*inp))
    print(res)
