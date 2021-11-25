class IntcodeComputer:
    def __init__(self, input):
        self.program = input.copy()
        self.initialProgram = input.copy()
        self.opIdx = 0
        self.ops = {
            1: self.add,
            2: self.multiply 
        }

    def alterInput(self,noun,verb):
        self.program[1] = noun
        self.program[2] = verb

    def refresh(self):
        self.program = self.initialProgram.copy()
        self.opIdx = 0
        
    def run(self):
        while self.program[self.opIdx] != 99:
            self.step()
        return self.program[0]

    def step(self):
        opCode = self.program[self.opIdx]
        op = self.ops[opCode]
        op()

    def add(self):
        x, y, outputIdx = self.getNextN(3)
        self.program[outputIdx] = self.program[x] + self.program[y]
        self.opIdx += 4

    def multiply(self):
        x, y, outputIdx = self.getNextN(3)
        self.program[outputIdx] = self.program[x] * self.program[y]
        self.opIdx += 4

    def getNextN(self, n):
        start, end = self.opIdx + 1, self.opIdx + n + 1
        return self.program[start:end]
