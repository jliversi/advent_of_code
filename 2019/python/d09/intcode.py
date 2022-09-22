class DefaultKeyDict(dict):
    def __init__(self, default_arg, *args):
        self.default_arg = default_arg
        dict.__init__(self, *args)

    def __getitem__(self, __k):
        if __k in self: 
            return super().__getitem__(__k)
        else:
            return self.default_arg

    def copy(self):
        return DefaultKeyDict(self.default_arg, super().copy())


class IntcodeComputer:
    def __init__(self, program_string, inputs=[]):
        self.setup_defaults(program_string)
        self.inputs = inputs
        
        self.ops = {
            1: self.add,
            2: self.multiply,
            3: self.get_input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.update_relative_offset,
            99: self.halt
        }

    def run(self):
        while True:
            self.step()
            if self.halted:
                return 'HALTED'

    def step(self):
        cur_op = self.program[self.op_idx]
        op_code, *params = self.parse_op_code(cur_op)
        op = self.ops[op_code]
        op(*params)
        

    # ops
    def add(self, param_a=0, param_b=0, param_c=0):
        x, y, output_idx = self.get_next_n(3)
        x = self.value_after_param(x, param_a)
        y = self.value_after_param(y, param_b)
        output_idx = self.output_idx_after_param(output_idx, param_c)
        self.program[output_idx] =  x + y
        self.op_idx += 4

    def multiply(self, param_a=0, param_b=0, param_c=0):
        x, y, output_idx = self.get_next_n(3)
        x = self.value_after_param(x, param_a)
        y = self.value_after_param(y, param_b)
        output_idx = self.output_idx_after_param(output_idx, param_c)
        self.program[output_idx] =  x * y
        self.op_idx += 4

    def get_input(self, param=0):
        output_idx = self.get_next_n(1)[0]
        output_idx = self.output_idx_after_param(output_idx, param)
        self.program[output_idx] = self.inputs.pop()
        self.op_idx += 2

    def output(self, param=0):
        x = self.get_next_n(1)[0]
        output = self.value_after_param(x, param)
        self.output_val = output
        print(output)
        self.op_idx += 2

    def jump_if_true(self,param_a=0,param_b=0):
        x, y = self.get_next_n(2)
        x = self.value_after_param(x, param_a)
        if x:
            y = self.value_after_param(y, param_b)
            self.op_idx = y
        else:
            self.op_idx += 3


    def jump_if_false(self,param_a=0,param_b=0):
        x, y = self.get_next_n(2)
        x = self.value_after_param(x, param_a)
        if not x:
            y = self.value_after_param(y, param_b)
            self.op_idx = y
        else:
            self.op_idx += 3

    def less_than(self,param_a=0,param_b=0,param_c=0):
        x, y, output_idx = self.get_next_n(3)
        x = self.value_after_param(x, param_a)
        y = self.value_after_param(y, param_b)
        output_idx = self.output_idx_after_param(output_idx, param_c)
        if x < y:
            self.program[output_idx] = 1
        else:
            self.program[output_idx] = 0
        self.op_idx += 4


    def equals(self,param_a=0,param_b=0,param_c=0):
        x, y, output_idx = self.get_next_n(3)
        x = self.value_after_param(x, param_a)
        y = self.value_after_param(y, param_b)
        output_idx = self.output_idx_after_param(output_idx, param_c)
        if x == y:
            self.program[output_idx] = 1
        else:
            self.program[output_idx] = 0
        self.op_idx += 4

    def update_relative_offset(self, param=0):
        inc = self.get_next_n(1)[0]
        inc = self.value_after_param(inc, param)
        self.relative_offset += inc
        self.op_idx += 2


    def halt(self):
        self.halted = True


    # internal helpers
    def parse_op_code(self, op_num):
        num_str = str(op_num)
        op_code = int(num_str[-2:])
        i = len(num_str) - 3
        params = []
        while i >= 0:
            params.append(int(num_str[i]))
            i -= 1
        return (op_code,) + tuple(params)

    def get_next_n(self, n):
        start, end = self.op_idx + 1, self.op_idx + n + 1
        result = []
        while start < end:
            result.append(self.program[start])
            start += 1
        return result

    def value_after_param(self, value, param):
        if param == 0:
            return self.program[value]
        elif param == 1:
            return value
        elif param == 2:
            return self.program[self.relative_offset + value]

    def output_idx_after_param(self, idx, param):
        if param == 0:
            return idx
        elif param == 2:
            return self.relative_offset + idx


    def setup_defaults(self, program_string):        
        program = DefaultKeyDict(0, {idx: int(x) for idx, x in enumerate(program_string.split(','))})
        self.program = program.copy()
        self.initial_program = program.copy()
        self.halted = False
        self.op_idx = 0
        self.output_val = None
        self.relative_offset = 0


    # external helpers
    def refresh(self):
        self.halted = False
        self.program = self.initial_program.copy()
        self.op_idx = 0
        self.relative_offset = 0


# class IntcodeComputer:
#     def __init__(self, programList, inputs=[]):
#         program = DefaultKeyDict(programList)
#         self.program = program.copy()
#         self.initialProgram = program.copy()
#         self.inputs = inputs
#         self.halted = False
#         self.opIdx = 0
#         self.outputVal = None
#         self.relativeOffset = 0
#         self.ops = {
#             1: self.add,
#             2: self.multiply,
#             3: self.getInput,
#             4: self.output,
#             5: self.jumpIfTrue,
#             6: self.jumpIfFalse,
#             7: self.lessThan,
#             8: self.equals,
#             9: self.updateRelativeOffset,
#             99: self.halt
#         }
        
#     def run(self):
#         if self.halted:
#             return 'HALTED'

#         while True:
#             stepOp = self.step()
#             if stepOp == 4:
#                 print(self.outputVal)
#             elif stepOp == 99:
#                 return 'HALTED'

#     def step(self):
#         opCode = self.parseOp(self.program[self.opIdx])
#         op = self.ops[opCode[0]]
#         op(*opCode[1:])
#         return opCode[0]

#     # Ops
    # def add(self, param_a=0, param_b=0):
    #     x, y, outputIdx = self.getNextN(3)
    #     x = self.valueAfterParam(x, param_a)
    #     y = self.valueAfterParam(y, param_b)
    #     self.program[outputIdx] =  x + y
    #     self.opIdx += 4

    # def multiply(self, param_a=0, param_b=0):
    #     x, y, outputIdx = self.getNextN(3)
    #     x = self.valueAfterParam(x, param_a)
    #     y = self.valueAfterParam(y, param_b)
    #     self.program[outputIdx] =  x * y
    #     self.opIdx += 4

    # def getInput(self, param=1):
    #     print('taking input')
    #     outputIdx = self.getNextN(1)[0]
    #     outputIdx = self.valueAfterParam(outputIdx,param)
    #     self.program[outputIdx] = self.inputs.pop()
    #     self.opIdx += 2

    # def output(self, param=0):
    #     print(self.opIdx)
    #     print('giving output')
    #     idx = self.getNextN(1)[0]
    #     output = self.valueAfterParam(idx, param)
    #     self.outputVal = output
    #     self.opIdx += 2

    # def jumpIfTrue(self,param_a=0,param_b=0):
    #     x, y = self.getNextN(2)
    #     x = self.valueAfterParam(x, param_a)
    #     if x:
    #         y = self.valueAfterParam(y, param_b)
    #         self.opIdx = y
    #     else:
    #         self.opIdx += 3


    # def jumpIfFalse(self,param_a=0,param_b=0):
    #     x, y = self.getNextN(2)
    #     x = self.valueAfterParam(x, param_a)
    #     if not x:
    #         y = self.valueAfterParam(y, param_b)
    #         self.opIdx = y
    #     else:
    #         self.opIdx += 3

    # def lessThan(self,param_a=0,param_b=0):
    #     x, y, outputIdx = self.getNextN(3)
    #     x = self.valueAfterParam(x, param_a)
    #     y = self.valueAfterParam(y, param_b)
    #     if x < y:
    #         self.program[outputIdx] = 1
    #     else:
    #         self.program[outputIdx] = 0
    #     self.opIdx += 4


    # def equals(self,param_a=0,param_b=0):
    #     x, y, outputIdx = self.getNextN(3)
    #     x = self.valueAfterParam(x, param_a)
    #     y = self.valueAfterParam(y, param_b)
    #     if x == y:
    #         self.program[outputIdx] = 1
    #     else:
    #         self.program[outputIdx] = 0
    #     self.opIdx += 4

    # def updateRelativeOffset(self, param=0):
    #     inc = self.getNextN(1)[0]
    #     inc = self.valueAfterParam(inc, param)
    #     self.relativeOffset += inc
    #     self.opIdx += 2


    # def halt(self):
    #     self.halted = True


#     # Internal helpers
    # def getNextN(self, n):
    #     start, end = self.opIdx + 1, self.opIdx + n + 1
    #     result = []
    #     while start < end:
    #         result.append(self.program[start])
    #         start += 1
    #     return result

#     def parseOp(self, num):
#         num = str(num)
#         opCode = int(num[-2:])
#         i = len(num) - 3
#         params = []
#         while i >= 0:
#             params.append(int(num[i]))
#             i -= 1
#         return (opCode,) + tuple(params)

#     def valueAfterParam(self, val, param):
#         if param == 0:
#             return self.program[val]
#         elif param == 1:
#             return val
#         elif param == 2:
#             return self.program[self.relativeOffset + val]
    
#     # External helpers
#     def addInput(self, input):
#         self.inputs = [input] + self.inputs

#     def refresh(self):
#         self.halted = False
#         self.program = self.initialProgram.copy()
#         self.opIdx = 0
#         self.relativeOffset = 0