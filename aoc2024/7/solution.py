def sum_correct(data):
    result = 0
    result2 = 0

    for res, nums in data:
        if is_correct(res, nums):
            result += res
        if is_correct2(res, nums):
            result2 += res

    return result, result2

def is_correct(res, nums):
    if len(nums) == 2:
        return res == nums[0] * nums[1] or res == sum(nums)

    return is_correct(res - nums[-1], nums[:-1]) or (not res % nums[-1] and is_correct(res // nums[-1], nums[:-1]))

def is_correct2(res, nums):
    if len(nums) == 2:
        return res == nums[0] * nums[1] or res == sum(nums) or res == int(str(nums[0]) + str(nums[1]))

    return is_correct2(res - nums[-1], nums[:-1]) or (
            not res % nums[-1] and is_correct2(res // nums[-1], nums[:-1])
    ) or (
        res % 10 ** len(str(nums[-1])) == nums[-1] and is_correct2(res // 10 ** len(str(nums[-1])), nums[:-1])
    )





def parse(data):
    result = []
    for line in data:
        splitted = line.strip().split(': ')
        result.append([int(splitted[0]), list(map(int, splitted[1].split(' ')))])

    return result

if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = sum_correct(test_1)
    print(res)
    assert res == (3749, 11387)

    res = sum_correct(inp)
    print(res)

