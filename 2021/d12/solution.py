# INPUT_FILE = 'test_input_1.txt'
# INPUT_FILE = 'test_input_2.txt'
# INPUT_FILE = 'test_input_3.txt'
INPUT_FILE = 'input.txt'

class Node:
    def __init__(self,val):
        self.val = val
        self.neighbors = []
        self.is_small = val.islower()
        self.is_start = val == 'start'
        self.is_end = val == 'end'

    def add_neighbor(self,other_node):
        if other_node not in self.neighbors:
            self.neighbors.append(other_node)

def parse_input(file_name):
    nodes = dict()
    with open(file_name, 'r') as f:
        for line in f.readlines():
            val1, val2 = line.strip().split('-')
            if val1 in nodes:
                node1 = nodes[val1]
            else:
                node1 = Node(val1)
                nodes[val1] = node1
            if val2 in nodes:
                node2 = nodes[val2]
            else:
                node2 = Node(val2)
                nodes[val2] = node2
            node1.add_neighbor(node2)
            node2.add_neighbor(node1)
    return nodes

def node_path_to_str(node_list):
    return '-'.join(map(lambda x: x.val, node_list))
            
def find_paths_1(cur_node, cur_path, visited, all_paths):
    cur_path.append(cur_node)
    if cur_node.is_end:
        node_str = node_path_to_str(cur_path)
        all_paths.add(node_str)
        return all_paths
    if cur_node.is_small:
        visited.add(cur_node)
    next_nodes = cur_node.neighbors
    for node in next_nodes:
        if node not in visited:
            find_paths_1(node, cur_path.copy(), visited.copy(), all_paths)
    return all_paths

def find_paths(cur_node, cur_path, visited, free_small_used, all_paths):
    cur_path.append(cur_node)
    if cur_node.is_end:
        node_str = node_path_to_str(cur_path)
        all_paths.add(node_str)
        return all_paths
    if cur_node.is_small:
        visited.add(cur_node)
    next_nodes = cur_node.neighbors
    for node in next_nodes:
        if node not in visited:
            find_paths(node, cur_path.copy(), visited.copy(), free_small_used, all_paths)
        elif not free_small_used and not node.is_start:
            find_paths(node, cur_path.copy(), visited.copy(), True, all_paths)
    return all_paths
    

def part_one(nodes):
    start_node = nodes['start']
    paths = find_paths_1(start_node, [], set(), set())

    print(len(paths))


def part_two(nodes):
    start_node = nodes['start']
    paths = find_paths(start_node, [], set([start_node]), False, set())
    print(len(paths))


def main():
    nodes = parse_input(INPUT_FILE)
    part_two(nodes)

if __name__ == '__main__':
    main()