directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def sum_traversed(matrix):
    result = 0

    for row in matrix:
        for cell in row:
            if cell == 'X':
                result += 1

    return result

def traverse(matrix):
    m, n = len(matrix), len(matrix[0])
    dirs = {'v': directions[1], '<': directions[2], '>': directions[0], '^': directions[3]}
    x, y = None, None
    for i in range(m):
        for j in range(n):
            if matrix[i][j] in dirs:
                y, x = i, j
                break
        if x is not None:
            break
    dir_i = directions.index(dirs[matrix[y][x]])

    def _traverse(x, y, dir_i, new_obs):
        visited = set()
        while True:
            if (x, y, dir_i) in visited:
                return True
            visited.add((x, y, dir_i))
            dy, dx = directions[dir_i]
            next_y, next_x = y + dy, x + dx
            if 0 <= next_x < n and 0 <= next_y < m:
                if matrix[next_y][next_x] != '#' and (next_x, next_y) != new_obs:
                    x, y = next_x, next_y
                else:
                    dir_i += 1
                    dir_i %= 4
            else:
                return False

    real_obs = 0
    checked_obs = {(x, y)}
    while True:
        matrix[y][x] = 'X'
        dy, dx = directions[dir_i]
        next_y, next_x = y + dy, x + dx
        if 0 <= next_x < n and 0 <= next_y < m:
            if matrix[next_y][next_x] != '#':
                if (next_x, next_y) not in checked_obs and _traverse(x, y, dir_i, (next_x, next_y)):
                    real_obs += 1
                checked_obs.add((next_x, next_y))
                x, y = next_x, next_y
            else:
                dir_i += 1
                dir_i %= 4
        else:
            break
    return sum_traversed(matrix), real_obs



def parse(data):
    result = []
    for line in data:
        result.append(list(line.strip()))

    return result

if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = traverse(test_1)
    print(res)
    assert res == (41, 6)

    res = traverse(inp)
    print(res)

