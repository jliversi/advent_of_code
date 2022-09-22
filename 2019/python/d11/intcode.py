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
    def __init__(self, int_list, inputs=[]):
        self.setup_defaults(int_list)
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
        self.outputs.append(output)
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


    def setup_defaults(self, int_list):        
        program = DefaultKeyDict(0, {idx: x for idx, x in enumerate(int_list)})
        self.program = program.copy()
        self.initial_program = program.copy()
        self.halted = False
        self.op_idx = 0
        self.outputs = []
        self.relative_offset = 0


    # external helpers
    def refresh(self):
        self.halted = False
        self.program = self.initial_program.copy()
        self.op_idx = 0
        self.relative_offset = 0
