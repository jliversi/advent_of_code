from functools import cache

# INPUT_FILE = 'input.txt'
INPUT_FILE = 'test_input.txt'

BASE_16_MAP = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def parse_input(file_name):
    with open(file_name, 'r') as f:
        return ''.join([BASE_16_MAP[char] for char in f.read()])

def chunk(iterable, chunk_size):
    result = []
    cur_set = None
    for i,el in enumerate(iterable):
        if i % chunk_size == 0:
            result.append(cur_set)
            cur_set = [el]
        else:
            cur_set.append(el)
    result.append(cur_set)
    return result[1:]

def literal_length(packet):
    # `packet` here starts with the version of some packet but may have plenty extra data afterward
    packet = packet[6:]
    chunked = chunk(packet,5)
    i = 0
    while chunked[i][0] != '0':
        i+= 1
    return ((i+1) * 5) + 6

def op_length(packet):
    # `packet` here starts with the version of some packet but may have plenty extra data afterward
    packet = packet[6:]


@cache
def op_arg_packets(packet):
    # `packet` here starts with the version of some packet but may have plenty extra data afterward
    packet = packet[6:]
    length_type_id = packet[6]
    args = []
    if length_type_id == '0':
        args_bit_count = int(packet[7:22],2)
        args_str = packet[22:args_bit_count+22]


def parse_literal(packet):
    v,t = int(packet[0:3],2), int(packet[3:6],2)
    last_5 = False
    i = 0
    num = []
    while not last_5:
        char = packet[i + 6]
        if i % 5 == 0:
            last_5 = char == '0'
        else:
            num.append(char)
        i += 1
    for x in range(4):
        num.append(packet[i + 6 + x])
    return {
        'v': v,
        't': t,
        'val': int(''.join(num),2)
    }


def parse_op(packet):
    v,t = int(packet[0:3],2), int(packet[3:6],2)
    args_packets = op_arg_packets(packet)
    args = list(map(lambda p: parse_packet(p), args_packets))

    return {
        'v': v,
        't': t,
        'args': args
    }

def parse_packet(packet):
    t = int(packet[3:6],2)
    if t == 4:
        return parse_literal(packet)
    else:
        return parse_op(packet)


def part_one(packet):
    print(literal_length(packet))
    # a = parse_packet(packet)
    # print(a)

def part_two():
    pass

def main():
    bin_string = parse_input(INPUT_FILE)
    part_one(bin_string)

if __name__ == '__main__':
    main()