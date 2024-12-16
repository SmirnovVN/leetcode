from collections import Counter


def cnt_stones(nums, k=25):
    nums = Counter(nums)
    for i in range(k):
        new_nums = Counter()
        for num, value in nums.items():
            if num == 0:
                new_nums[1] += value
            elif len(str(num)) % 2 == 0:
                s = str(num)
                new_nums[int(s[:len(s)//2])] += value
                new_nums[int(s[len(s)//2:])] += value
            else:
                new_nums[num * 2024] += value

        nums = new_nums

    return sum(nums.values())


def parse(data):
    for line in data:
        return list(map(int, line.strip().split(' ')))


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = cnt_stones(test_1)
    print(res)
    assert res == 55312

    res = cnt_stones(inp)
    print(res)

    res = cnt_stones(inp, k=75)
    print(res)
