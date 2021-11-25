INPUT = (278384,824795)


def digits(num):
    return [int(x) for x in str(num)]


def has_double(digs):
    for i in range(len(digs)):
        if i == len(digs) - 1:
            return False
        elif digs[i] == digs[i + 1]:
            return True

def ascending(digs):
    for i in range(len(digs)):
        if i == len(digs) - 1:
            return True 
        elif digs[i] > digs[i + 1]:
            return False 

def check_num(num):
    digs = digits(num)
    return has_double(digs) and ascending(digs)


def solve():
    total = 0
    for i in range(INPUT[0], INPUT[1]):
        if check_num(i):
            total += 1
    return total

print(solve())
    
