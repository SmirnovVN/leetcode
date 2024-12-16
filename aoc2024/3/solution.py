import re


def sum_up(nums):
    result = 0

    for i, j in nums:
        result += i * j

    return result


def parse(file):
    nums = []
    for line in file:
        pattern = re.compile('mul\(\d{1,3},\d{1,3}\)')
        muls = pattern.findall(line)
        for mul in muls:
            extract = re.compile(r'\d{1,3}')
            numbers = extract.findall(mul)
            nums.append((int(numbers[0]), int(numbers[1])))
    return nums

def parse2(file):
    nums = []
    do = True
    for line in file:
        pattern = re.compile("(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))")
        instructions = pattern.findall(line)
        for i in instructions:
            if i == "don't()":
                do = False
            elif i == "do()":
                do = True
            elif do:
                extract = re.compile(r'\d{1,3}')
                numbers = extract.findall(i)
                nums.append((int(numbers[0]), int(numbers[1])))
    return nums

if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    res = sum_up(test_1)
    print(res)
    assert res == 161

    res = sum_up(test_2)
    print(res)
    assert res == 100161

    res = sum_up(inp)
    print(res)


    with open('test_1.txt') as file:
        test_1 = parse2(file)
    with open('test_2.txt') as file:
        test_2 = parse2(file)
    with open('input.txt') as file:
        inp = parse2(file)

    res = sum_up(test_1)
    print(res)
    assert res == 161

    res = sum_up(test_2)
    print(res)
    assert res == 100048

    res = sum_up(inp)
    print(res)
