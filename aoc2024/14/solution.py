import re
from time import sleep

import numpy as np

from matplotlib import pyplot as plt

def move(robots, seconds, wide, tall):
    matrix = [[0]*wide for _ in range(tall)]

    for x, y, vx, vy in robots:
        matrix[(y + seconds * vy) % tall][(x + seconds * vx) % wide] += 1

    return matrix


def safety(matrix, wide, tall):
    a = sum(sum(row[:wide//2]) for row in matrix[:tall//2])
    b = sum(sum(row[wide//2 + 1:]) for row in matrix[:tall//2])
    c = sum(sum(row[:wide//2]) for row in matrix[tall//2 + 1:])
    d = sum(sum(row[wide//2 + 1:]) for row in matrix[tall//2 + 1:])

    return a * b * c * d


def parse(file):
    result = []
    for line in file:
        extract = re.compile(r'-?\d+')
        numbers = extract.findall(line)
        result.append(list(map(int, numbers)))
    return result


def visualise(matrix, second):

    data = np.array([[[0,255,0] if cell else [0,0,0] for cell in row] for row in matrix])

    plt.figure(1)
    plt.clf()
    plt.imshow(data)
    plt.title('second ' + str(second))
    plt.pause(0.5)
    plt.savefig(f'egg{i}.png')


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = safety(move(test_2, 100, 11, 7), 11, 7)
    print(res)
    assert res == 12

    res = safety(move(inp, 100, 101, 103), 101, 103)
    print(res)
    for i in range(20000):
        res = move(inp, i, 101, 103)
        s = safety(res, wide=101, tall=103)
        if s < 200000000:
            visualise(res, s)
