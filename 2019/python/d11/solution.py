from sys import argv
from intcode import IntcodeComputer

   

def get_input(file_name):
    with open(file_name) as f:
        input = [int(x) for x in f.read().split(',')]
    return input
        

def run(file_name):
    print('Getting input')
    input = get_input(file_name)

if __name__ == "__main__":
   r = run(argv[1])
