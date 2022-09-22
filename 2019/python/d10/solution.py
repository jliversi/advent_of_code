from sys import argv
from math import pi, sqrt, atan2

def pos(num):
    if num == 0:
        return num
    elif num > 0:
        return 1
    elif num < 0:
        return -1

def colinear(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    if x1 == 0 and x2 == 0:
        return True
    elif y1 == 0 and y2 == 0:
        return True
    elif x1 == 0 or x2 == 0:
        return False
    elif y1 == 0 or y2 == 0:
        return False
    
    return x1/x2 == y1/y2

def same_dir(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return pos(x1) == pos(x2) and pos(y1) == pos(y2)

def seen_as_one(v1, v2):
    return colinear(v1, v2) and same_dir(v1, v2)

def v_from_node(node,  other_node):
    x1, y1 = node
    x2, y2 = other_node
    return x2 - x1, y2 - y1

def dist(node):
    x, y = node
    return sqrt(x**2 + y**2)

def seen(node, node_set):
    rel_set = [v_from_node(node, other_node) for other_node in node_set if other_node != node]
    seen_or_blocked = set()
    seen_grouped = []
    for n1 in rel_set:
        if n1 in seen_or_blocked: continue
        seen_with_n1 = [n1]
        for n2 in rel_set:
            if n2 == n1: continue
            if seen_as_one(n1, n2): seen_with_n1.append(n2)
        
        for x in seen_with_n1: seen_or_blocked.add(x)
        seen_grouped.append(seen_with_n1)
    
    return list(map(lambda group: list(sorted(group, key=lambda x: dist(x) * -1)), seen_grouped))
    # return list(map(lambda group: min(group, key=lambda x: dist(x)), seen_grouped))

def build_result(node_set):
    result = dict()
    for node in node_set:
        result[node] = seen(node, node_set)
    return result

def get_count_map(result_dict):
    return {k: len(v) for k, v in result_dict.items()}

def best_in_count_map(cm):
    max = 0
    best = None
    for k, v in cm.items():
        if v > max:
            max = v
            best = k
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

def angle(v):
    x,y = v 
    return atan2(x,y)

def laser_and_remove(station, lists):
    sx, sy = station
    i = 1
    while any(lists):
        for el in lists:
            if el:
                coords = el.pop()
                x, y = coords
                asteroid_destroyed = sx + x, sy + y
                print(f'{i}: {asteroid_destroyed} destroyed')
                i += 1


def run(file_name):
    print('Getting input')
    input = get_input(file_name)
    print('Building result dictionary')
    result_dict = build_result(input)
    count_map = get_count_map(result_dict)
    station_location = best_in_count_map(count_map)
    print(f'Station location chosen at {station_location}')
    target_lists = sorted(result_dict[station_location], key=lambda x: pi - angle(x[0]))
    print('Beginning asteroid removal')
    laser_and_remove(station_location, target_lists.copy())
    return result_dict

if __name__ == "__main__":
   r = run(argv[1])
