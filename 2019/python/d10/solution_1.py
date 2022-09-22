from sys import argv
from math import gcd

def s_reduce(x,y):
    z = gcd(abs(x),abs(y))
    if z == 1:
        return x,y
    else:
        return x/z,y/z
# node_1 should always be "first" in a top-bottom, left-right order
def get_slope(node_1, node_2):
    x1, y1 = node_1
    x2, y2 = node_2
    x, y = (x2 - x1), (y2 - y1)
    if x == 0:
        return '1-0'
    elif y == 0:
        return '0-1'

    x, y = s_reduce(x,y)
    return f'{str(int(y))}-{str(int(x))}'

def build_result(input):
    result = {}
    finished_nodes = set()
    for node in input:
        process_node(node, input, result, finished_nodes)
        finished_nodes.add(node)
    return result

def process_node(node, input, result, finished_nodes):
    for other_node in input:
        if other_node == node:
            continue
        elif other_node in finished_nodes:
            continue
        
        slope = get_slope(node, other_node)
        add_to_result(node, other_node, slope, result)
        

def add_to_result(node, other_node, slope, result):
    if node in result:
        if slope in result[node]:
            result[node][slope].append(other_node)
        else:
            result[node][slope] = [other_node]
    else:
        result[node] = {
            slope: [other_node]
        }
    
    if other_node in result:
        if slope in result[other_node]:
            result[other_node][slope].append(node)
        else:
            result[other_node][slope] = [node]
    else:
        result[other_node] = {
            slope: [node]
        }
    
def true_seen_count(node, slope_dict):
    count = 0
    for v in slope_dict.values():
        if node > v[0] and node < v[-1]:
            count += 2
        else: 
            count += 1
    return count

def get_count_map(result_dict):
    count_map = {k: true_seen_count(k, v) for k, v in result_dict.items()}
    return count_map


def best_in_count_map(cm):
    max = 0
    best = None
    for k, v in cm.items():
        if v > max:
            max = v
            best = (k,v)
    return best


def get_input(file_name):
    input_nodes = []
    with open(file_name) as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line):
                if char == '#':
                    input_nodes.append((x,y))
    return input_nodes


def print_count_map(count_map, file_name):
    with open(file_name) as f:
        visual = []
        for y, line in enumerate(f):
            new_line = ''
            for x, char in enumerate(line):
                if char == '#':
                    new_line += str(count_map[(x,y)])
                else:
                    new_line += char
            visual.append(new_line)
        
    print('Count map:')
    for l in visual:
        print(l)
    print('--------------')

def run(file_name):
    input = get_input(file_name)
    result_dict = build_result(input)
    count_map = get_count_map(result_dict)
    winner, count = best_in_count_map(count_map)
    print_count_map(count_map, file_name)
    print(f'Winner was {winner} with a total of {count} seen')
    return result_dict

if __name__ == "__main__":
   r = run(argv[1])

    
    
# # dict I'm building
# {
#     node: {
#         slope_1: [other_node_1, other_node_3],
#         slope_2: [other_node_2]
#     },
#     # ex
#     (0,0): {
#         a: [(3,1), (6,2), ]
#     }
# }


