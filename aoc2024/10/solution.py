
from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def sum_up(nums):
    m, n = len(nums), len(nums[0])
    dp = [[set() for _ in range(n)] for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 9:
                dp[i][j].add((i, j))
                q.append((i, j, 9))
    visited = set()
    while q:
        i, j, num = q.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for di, dj in directions:
            ni, nj, nnum = i + di, j + dj, num - 1
            if 0 <= ni < m and 0 <= nj < n and nums[ni][nj] == nnum:
                dp[ni][nj].update(dp[i][j])
                q.append((ni, nj, nnum))


    result = 0
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 0:
                result += len(dp[i][j])

    return result

def sum_up2(nums):
    m, n = len(nums), len(nums[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 9:
                dp[i][j] = 1
                q.append((i, j, 9))
    visited = set()
    while q:
        i, j, num = q.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for di, dj in directions:
            ni, nj, nnum = i + di, j + dj, num - 1
            if 0 <= ni < m and 0 <= nj < n and nums[ni][nj] == nnum:
                dp[ni][nj] += dp[i][j]
                q.append((ni, nj, nnum))


    result = 0
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 0:
                result += dp[i][j]

    return result



def parse(data):
    result = []
    for line in data:
        result.append(list(map(int, line.strip())))

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
    assert res == 36

    res = sum_up2(test_2)
    print(res)
    assert res == 81

    res = sum_up(inp)
    print(res)

    res = sum_up2(inp)
    print(res)
