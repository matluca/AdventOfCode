def get_n_parameters(opcode):
    if opcode in [1, 2, 7, 8]:
        return 3
    if opcode in [5, 6]:
        return 2
    if opcode in [3, 4, 9]:
        return 1
    if opcode in [99]:
        return 0


class Intcode:
    def __init__(self, program, inputs=None):
        if input is None:
            self.input = []
        else:
            self.input = inputs
        self.program = {i: v for i, v in enumerate(program)}
        self.output = []
        self.halted = False
        self.pointer = 0
        self.relative_base = 0
        self.opcode_map = {
            1: self.add,
            2: self.mul,
            3: self.inp,
            4: self.out,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_then,
            8: self.equals,
            9: self.adjust_relative_base,
            99: self.halt,
        }

    def decode_opcode(self):
        opcode = self.program[self.pointer] % 100
        n_parameters = get_n_parameters(opcode)
        modes = [0] * n_parameters
        r = self.program[self.pointer] // 100
        i = 0
        while r > 0:
            modes[i] = r % 10
            r = r // 10
            i += 1
        return opcode, modes

    def value(self, pointer, mode):
        if mode == 0 and pointer in self.program.keys() and self.program[pointer] in self.program.keys():
            return self.program[self.program[pointer]]
        if mode == 1 and pointer in self.program.keys():
            return self.program[pointer]
        if mode == 2:
            p = self.program[pointer] + self.relative_base
            if p in self.program.keys():
                return self.program[p]
        return 0

    def add(self, modes):
        self.set(self.program[self.pointer + 3], modes[2], self.value(self.pointer + 1, modes[0]) + self.value(
            self.pointer + 2, modes[1]))
        self.pointer += 4

    def set(self, pointer, mode, value):
        if mode == 2:
            self.program[pointer + self.relative_base] = value
        else:
            self.program[pointer] = value

    def mul(self, modes):
        self.set(self.program[self.pointer + 3], modes[2], self.value(self.pointer + 1, modes[0]) * self.value(
            self.pointer + 2, modes[1]))
        self.pointer += 4

    def inp(self, modes):
        self.set(self.program[self.pointer + 1], modes[0], self.input.pop(0))
        self.pointer += 2

    def out(self, modes):
        self.output.append(self.value(self.pointer + 1, modes[0]))
        self.pointer += 2

    def jump_if_true(self, modes):
        if self.value(self.pointer + 1, modes[0]) != 0:
            self.pointer = self.value(self.pointer + 2, modes[1])
        else:
            self.pointer += 3

    def jump_if_false(self, modes):
        if self.value(self.pointer + 1, modes[0]) == 0:
            self.pointer = self.value(self.pointer + 2, modes[1])
        else:
            self.pointer += 3

    def less_then(self, modes):
        if self.value(self.pointer + 1, modes[0]) < self.value(self.pointer + 2, modes[1]):
            self.set(self.program[self.pointer + 3], modes[2], 1)
        else:
            self.set(self.program[self.pointer + 3], modes[2], 0)
        self.pointer += 4

    def equals(self, modes):
        if self.value(self.pointer + 1, modes[0]) == self.value(self.pointer + 2, modes[1]):
            self.set(self.program[self.pointer + 3], modes[2], 1)
        else:
            self.set(self.program[self.pointer + 3], modes[2], 0)
        self.pointer += 4

    def adjust_relative_base(self, modes):
        self.relative_base += self.value(self.pointer + 1, modes[0])
        self.pointer += 2

    def halt(self, _):
        self.halted = True

    def execute(self):
        opcode, modes = self.decode_opcode()
        self.opcode_map[opcode](modes)

    def run(self):
        while not self.halted:
            self.execute()
