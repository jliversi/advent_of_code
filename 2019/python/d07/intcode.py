class IntcodeComputer:
    def __init__(self, program, inputs=[]):
        self.program = program.copy()
        self.initialProgram = program.copy()
        self.inputs = inputs
        self.halted = False
        self.opIdx = 0
        self.outputVal = None
        self.ops = {
            1: self.add,
            2: self.multiply,
            3: self.getInput,
            4: self.output,
            5: self.jumpIfTrue,
            6: self.jumpIfFalse,
            7: self.lessThan,
            8: self.equals,
            99: self.halt
        }
        
    def run(self):
        if self.halted:
            return 'HALTED'

        while True:
            stepOp = self.step()
            if stepOp == 4:
                return self.outputVal
            elif stepOp == 99:
                return 'HALTED'

    def step(self):
        opCode = self.parseOp(self.program[self.opIdx])
        op = self.ops[opCode[0]]
        op(*opCode[1:])
        return opCode[0]

    # Ops
    def add(self, param_a=0, param_b=0):
        x, y, outputIdx = self.getNextN(3)
        x = x if param_a else self.program[x]
        y = y if param_b else self.program[y]
        self.program[outputIdx] =  x + y
        self.opIdx += 4

    def multiply(self, param_a=0, param_b=0):
        x, y, outputIdx = self.getNextN(3)
        x = x if param_a else self.program[x]
        y = y if param_b else self.program[y]
        self.program[outputIdx] =  x * y
        self.opIdx += 4

    def getInput(self):
        print('taking input')
        outputIdx = self.getNextN(1)[0]
        self.program[outputIdx] = self.inputs.pop()
        self.opIdx += 2

    def output(self, param=0):
        print('giving output')
        idx = self.getNextN(1)[0]
        output = idx if param else self.program[idx]
        self.outputVal = output
        self.opIdx += 2

    def jumpIfTrue(self,param_a=0,param_b=0):
        x, y = self.getNextN(2)
        x = x if param_a else self.program[x]
        if x:
            y = y if param_b else self.program[y]
            self.opIdx = y
        else:
            self.opIdx += 3


    def jumpIfFalse(self,param_a=0,param_b=0):
        x, y = self.getNextN(2)
        x = x if param_a else self.program[x]
        if not x:
            y = y if param_b else self.program[y]
            self.opIdx = y
        else:
            self.opIdx += 3

    def lessThan(self,param_a=0,param_b=0):
        x, y, outputIdx = self.getNextN(3)
        x = x if param_a else self.program[x]
        y = y if param_b else self.program[y]
        if x < y:
            self.program[outputIdx] = 1
        else:
            self.program[outputIdx] = 0
        self.opIdx += 4


    def equals(self,param_a=0,param_b=0):
        x, y, outputIdx = self.getNextN(3)
        x = x if param_a else self.program[x]
        y = y if param_b else self.program[y]
        if x == y:
            self.program[outputIdx] = 1
        else:
            self.program[outputIdx] = 0
        self.opIdx += 4

    def halt(self):
        self.halted = True


    # Internal helpers
    def getNextN(self, n):
        start, end = self.opIdx + 1, self.opIdx + n + 1
        return self.program[start:end]

    def parseOp(self, num):
        num = str(num)
        opCode = int(num[-2:])
        i = len(num) - 3
        params = []
        while i >= 0:
            params.append(int(num[i]))
            i -= 1
        return (opCode,) + tuple(params)
    
    # External helpers
    def addInput(self, input):
        self.inputs = [input] + self.inputs

    def refresh(self):
        self.halted = False
        self.program = self.initialProgram.copy()
        self.opIdx = 0