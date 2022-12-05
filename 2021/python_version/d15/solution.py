INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input.txt'

DIRS = (
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
)

def parse_input(file_name):
    with open(file_name, 'r') as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]

def print_progress(unvisited):
    total_percent = 100 - ((len(unvisited) / 250000)  * 100)
    if total_percent % 1 == 0:
        print(f'{total_percent}% complete')


def increment_graph(graph):
    return [[x + 1 if x < 9 else 1 for x in row] for row in graph]

def build_full_graph(partial_graph):
    a = partial_graph
    b = increment_graph(a)
    c = increment_graph(b)
    d = increment_graph(c)
    e = increment_graph(d)
    top_row = [a[i] + b[i] + c[i] + d[i] + e[i] for i in range(len(a))]
    a = top_row
    b = increment_graph(a)
    c = increment_graph(b)
    d = increment_graph(c)
    e = increment_graph(d)
    return a + b + c + d + e

def build_unvisited_set(dim_x, dim_y):
    result = set()
    for x in range(dim_x):
        for y in range(dim_y):
            result.add((x,y))
    return result

def build_dists_dict(dim_x, dim_y):
    result = dict()
    for x in range(dim_x):
        for y in range(dim_y):
            result[(x,y)] = float('inf')
    result[(0,0)] = 0
    return result

def nbrs(coord, dim_x, dim_y):
    x,y = coord
    result = []
    for dx,dy in DIRS:
        new_x, new_y = x + dx, y + dy
        if new_x in range(dim_x) and new_y in range(dim_y):
            result.append((new_x, new_y))
    return result

def find_min_node(unvisited, dists, seen):
    smallest = None
    smallest_dist = float('inf')
    search_space = seen.intersection(unvisited)
    for node in search_space:
        if dists[node] < smallest_dist:
            smallest = node
            smallest_dist = dists[node]
    return smallest

def find_min_node(possible_next_nodes, dists):
    smallest = None
    smallest_dist = float('inf')
    for node in possible_next_nodes:
        if dists[node] < smallest_dist:
            smallest = node
            smallest_dist = dists[node]
    return smallest

def djikstras(graph):
    dim_x, dim_y = len(graph), len(graph[0])
    destination = (dim_x - 1, dim_y - 1)
    dists = build_dists_dict(dim_x, dim_y)
    unvisited = build_unvisited_set(dim_x, dim_y)
    possible_next_nodes = {(0,0)}
    while destination in unvisited:
        print_progress(unvisited)
        current = find_min_node(possible_next_nodes, dists)
        possible_next_nodes.remove(current)
        unvisited.remove(current)
        for nbr in filter(lambda x: x in unvisited, nbrs(current, dim_x, dim_y)):
            nbr_x,nbr_y = nbr
            nbr_val = graph[nbr_x][nbr_y]
            dist_from_cur = dists[current] + nbr_val
            if dist_from_cur < dists[nbr]:
                possible_next_nodes.add(nbr)
                dists[nbr] = dist_from_cur
    return dists

def part_one(graph):
    dists = djikstras(graph)
    dim_x, dim_y = len(graph), len(graph[0])
    print(dists[(dim_x - 1,dim_y - 1)])

def part_two(partial_graph):
    full_graph = build_full_graph(partial_graph)
    dists = djikstras(full_graph)
    dim_x, dim_y = len(full_graph), len(full_graph[0])
    print(dists[(dim_x - 1,dim_y - 1)])


def main():
    graph = parse_input(INPUT_FILE)
    part_two(graph)

if __name__ == '__main__':
    main()