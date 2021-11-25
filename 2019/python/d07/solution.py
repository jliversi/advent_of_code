from intcode import IntcodeComputer
from itertools import permutations

with open('input.txt') as f:
    INPUT = [int(x) for x in f.read().split(',')]


# INPUT = [int(x) for x in '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'.split(',')]


POSSES = permutations([5,6,7,8,9])

def runner(seq):
    a = IntcodeComputer(INPUT, [0,seq[0]])
    b = IntcodeComputer(INPUT, [seq[1]])
    c = IntcodeComputer(INPUT, [seq[2]])
    d = IntcodeComputer(INPUT, [seq[3]])
    e = IntcodeComputer(INPUT, [seq[4]])
    results = []
    while 'HALTED' not in results:
        a_result = a.run()
        b.addInput(a_result)
        b_result = b.run()
        c.addInput(b_result)
        c_result = c.run()
        d.addInput(c_result)
        d_result = d.run()
        e.addInput(d_result)
        e_result = e.run()
        a.addInput(e_result)
        results = results + [a_result, b_result, c_result, d_result, e_result]
    return max([x for x in results if x != 'HALTED'])
        
# print(runner((9,8,7,6,5)))

print(max([runner(x) for x in POSSES]))






# def run(seq):
#     a = IntcodeComputer(INPUT, [0,seq[0]])
#     b = IntcodeComputer(INPUT, [a.run(), seq[1]])
#     c = IntcodeComputer(INPUT, [b.run(), seq[2]])
#     d = IntcodeComputer(INPUT, [c.run(), seq[3]])
#     e = IntcodeComputer(INPUT, [d.run(), seq[4]])
#     return e.run()