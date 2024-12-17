import re


class Computer:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.pointer = 0
        self.output = []
        self.opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }

    def run(self, instr):
        while True:
            operand = instr[self.pointer + 1]
            self.opcodes[instr[self.pointer]](operand)
            self.pointer += 2
            if self.pointer >= len(instr):
                break

        return self.output

    def combo(self, operand):
        """
        Combo operands 0 through 3 represent literal values 0 through 3.
        Combo operand 4 represents the value of register A.
        Combo operand 5 represents the value of register B.
        Combo operand 6 represents the value of register C.
        Combo operand 7 is reserved and will not appear in valid programs.
        :param operand:
        :return:
        """
        if operand <= 3:
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        if operand == 7:
            raise ValueError('Combo operand 7 is reserved and will not appear in valid programs')

    def dv(self, operand):
        return int(self.a / 2 ** self.combo(operand))

    def adv(self, operand):
        """
        The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
        The denominator is found by raising 2 to the power of the instruction's combo operand.
        (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
        The result of the division operation is truncated to an integer and then written to the A register.
        """
        self.a = self.dv(operand)

    def bxl(self, operand):
        """
        The bxl instruction (opcode 1) calculates the bitwise XOR of register B
        and the instruction's literal operand, then stores the result in register B.
        """
        self.b = self.b ^ operand

    def bst(self, operand):
        """
        The bst instruction (opcode 2) calculates the value of its combo operand modulo 8
        (thereby keeping only its lowest 3 bits), then writes that value to the B register.
        """
        self.b = self.combo(operand) % 8

    def jnz(self, operand):
        """
        The jnz instruction (opcode 3) does nothing if the A register is 0.
        However, if the A register is not zero, it jumps by setting the instruction
        pointer to the value of its literal operand;
        if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        """
        if self.a:
            self.pointer = operand - 2

    def bxc(self, _):
        """
        The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C,
        then stores the result in register B.
        (For legacy reasons, this instruction reads an operand but ignores it.)
        """
        self.b = self.b ^ self.c

    def out(self, operand):
        """
        The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
        then outputs that value. (If a program outputs multiple values, they are separated by commas.)
        """
        self.output.append(self.combo(operand) % 8)

    def bdv(self, operand):
        """
        The bdv instruction (opcode 6) works exactly like the adv instruction except
        that the result is stored in the B register. (The numerator is still read from the A register.)
        """
        self.a = self.dv(operand)

    def cdv(self, operand):
        """
        The cdv instruction (opcode 7) works exactly like the
        adv instruction except that the result is stored in the C register.
        (The numerator is still read from the A register.)
        """
        self.c = self.dv(operand)


def parse(file):
    result = []
    for line in file:
        if line == '\n':
            continue
        extract = re.compile(r'\d+')
        numbers = extract.findall(line)
        if len(numbers) > 1:
            result.append(list(map(int, numbers)))
        else:
            result.append(int(numbers[0]))
    return result


def find_a(data):
    candidates = [0]
    for length in range(1, len(data[3]) + 1):
        out = []
        for num in candidates:
            for offset in range(8):
                a = 8 * num + offset
                if Computer(a, data[1], data[2]).run(data[3]) == data[3][-length:]:
                    out.append(a)

        candidates = out

    data[0] = min(candidates)


if __name__ == '__main__':
    with open('test_1.txt') as file:
        test_1 = parse(file)
    with open('test_2.txt') as file:
        test_2 = parse(file)
    with open('input.txt') as file:
        inp = parse(file)

    comp = Computer(test_1[0], test_1[1], test_1[2])
    res = comp.run(test_1[3])
    print(','.join(map(str, res)))
    assert ','.join(map(str, res)) == '4,6,3,5,6,3,5,2,1,0'

    comp = Computer(inp[0], inp[1], inp[2])
    res = comp.run(inp[3])
    print(','.join(map(str, res)))

    find_a(test_2)
    print(test_2[0])
    assert test_2[0] == 117440

    find_a(inp)
    comp = Computer(inp[0], inp[1], inp[2])
    res = comp.run(inp[3])
    assert res == inp[3]
    print(inp[0])
