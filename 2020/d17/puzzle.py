space = dict()
nbr_memo = dict()

with open('input.txt') as f:
  row = 0
  for l in f:
    col = 0
    for char in l:
      pnt = (row, col, 0, 0)
      if char == '#':
        space[pnt] = True
      elif char == '.':
        space[pnt] = False
      col += 1
    row += 1

# generate 80 directions
NBR_DIRS = []
for x in [-1, 0, 1]:
  for y in [-1, 0, 1]:
    for z in [-1, 0, 1]:
      for w in [-1, 0, 1]:
        NBR_DIRS.append((x,y,z,w))

NBR_DIRS.remove((0,0,0,0))

def neighbors(x,y,z,w):
  if (x,y,z,w) in nbr_memo:
    return nbr_memo[(x,y,z,w)]
  result = []
  for direc in NBR_DIRS:
    dx, dy, dz, dw = direc
    nbr = (x + dx, y + dy, z + dz, w + dw)
    result.append(nbr)
  nbr_memo[(x,y,z,w)] = result
  return result

def nbr_on_count(x,y,z,w):
  total = 0
  for el in neighbors(x,y,z,w):
    if el in space and space[el]:
      total += 1
  return total

def total_count():
  total = 0
  for k in space:
    if space[k]:
      total += 1
  return total

def run_round():
  # add edge neighbors
  to_add = []
  for node in space:
    for nbr in neighbors(*node):
      if nbr not in space:
        to_add.append(nbr)
  for nbr in to_add:
    space[nbr] = False
  
  # check every node, determine which need to flip
  to_false = []
  to_true = []
  for node in space:
    cur_val = space[node]
    nbr_count = nbr_on_count(*node)
    if cur_val and nbr_count not in [2,3]:
      to_false.append(node)
    elif not cur_val and nbr_count == 3:
      to_true.append(node)
  
  # flip needed flips
  for node in to_false:
    space[node] = False
  for node in to_true:
    space[node] = True


for i in range(6):
  print(total_count())
  run_round()

print(total_count())








# # FOR 3D

# FACES = (
#   (1,0,0),
#   (-1,0,0),
#   (0,1,0),
#   (0,-1,0),
#   (0,0,1),
#   (0,0,-1)
# )

# EDGES = (
#   (0,1,1),
#   (0,1,-1),
#   (0,-1,1),
#   (0,-1,-1),
#   (1,0,1),
#   (1,0,-1),
#   (-1,0,1),
#   (-1,0,-1),
#   (1,1,0),
#   (1,-1,0),
#   (-1,1,0),
#   (-1,-1,0)
# )

# CORNERS = (
#   (1,1,1),
#   (1,1,-1),
#   (1,-1,1),
#   (1,-1,-1),
#   (-1,1,1),
#   (-1,1,-1),
#   (-1,-1,1),
#   (-1,-1,-1)
# )

# ALL = [FACES, EDGES, CORNERS]

# def neighbors(x,y,z):
#   if (x,y,z) in nbr_memo:
#     return nbr_memo[(x,y,z)]
#   result = []
#   for el in ALL:
#     for direc in el:
#       dx, dy, dz = direc
#       nbr = (x + dx, y + dy, z + dz)
#       result.append(nbr)
#   nbr_memo[(x,y,z)] = result
#   return result

# def nbr_on_count(x,y,z):
#   total = 0
#   for el in neighbors(x,y,z):
#     if el in space and space[el]:
#       total += 1
#   return total

# def total_count():
#   total = 0
#   for k in space:
#     if space[k]:
#       total += 1
#   return total

# def run_round():
#   # add edge neighbors
#   to_add = []
#   for node in space:
#     for nbr in neighbors(*node):
#       if nbr not in space:
#         to_add.append(nbr)
#   for nbr in to_add:
#     space[nbr] = False
  
#   # check every node, determine which need to flip
#   to_false = []
#   to_true = []
#   for node in space:
#     cur_val = space[node]
#     nbr_count = nbr_on_count(*node)
#     if cur_val and nbr_count not in [2,3]:
#       to_false.append(node)
#     elif not cur_val and nbr_count == 3:
#       to_true.append(node)
  
#   # flip needed flips
#   for node in to_false:
#     space[node] = False
#   for node in to_true:
#     space[node] = True


# for i in range(6):
#   print(total_count())
#   run_round()

# print(total_count())
  

