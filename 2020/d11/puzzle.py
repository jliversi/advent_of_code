DIRS = [
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
  [0, -1],
  [-1, -1],
]

with open('input.txt','r') as f:
  GRID = []
  for l in f:
    GRID.append(list(l.replace('\n','')))


def print_grid():
  for el in GRID:
    print(el)


I_MAX = len(GRID) - 1
J_MAX = len(GRID[0]) - 1

def num_occ_neighbors(i,j):
  total = 0
  for di, dj in DIRS:
    nbr_i = i + di
    nbr_j = j + dj
    if nbr_i not in range(0, I_MAX + 1) or nbr_j not in range(0, J_MAX + 1):
      continue
    elif GRID[nbr_i][nbr_j] == '#':
      total += 1
  return total


def num_occ_neighbors2(i,j):
  
  total = 0
  for di, dj in DIRS:
    nbr_i = i + di
    nbr_j = j + dj
    
    while nbr_i in range(0, I_MAX + 1) and nbr_j in range(0, J_MAX + 1):
      nbr = GRID[nbr_i][nbr_j]
      if nbr == '#':
        total += 1
        break
      elif nbr == 'L':
        break
      else:
        nbr_i += di
        nbr_j += dj
  return total

def run_round():
  to_fill = []
  to_empty = []
  for idx1 in range(0,len(GRID)):
    for idx2 in range(0,len(GRID[0])):
      ele = GRID[idx1][idx2]
      if ele == '.':
        continue
      count = num_occ_neighbors2(idx1, idx2)
      if ele == '#' and count > 4:
        to_empty.append([idx1,idx2])
      elif ele == 'L' and count == 0:
        to_fill.append([idx1, idx2])
  
  if (len(to_fill) + len(to_empty)) == 0:
    return False
  
  
  for el in to_fill:
    x, y = el
    GRID[x][y] = '#'
  for el in to_empty:
    x, y = el
    GRID[x][y] = 'L'
  return True


def total_occ():
  total = 0
  for row in GRID:
    for seat in row:
      if seat == '#':
        total += 1
  return total


unstable = True
round_num = 1
while unstable:
  round_num += 1
  unstable = run_round()

print('rounds', round_num)

print('\n',total_occ())