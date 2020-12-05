inputs = []

with open('input.txt', 'r') as f:
  for l in f:
    inputs.append(l)

inputs = list(map(lambda x: x.rstrip(), inputs))

def num_trees_hit(inputs, dx, dy):
  l_length = len(inputs[0])
  cur_h_idx = 0
  cur_v_idx = 0
  count = 0
  for l in inputs:
    if cur_v_idx >= len(inputs):
      break
    char = inputs[cur_v_idx][cur_h_idx]
    if char == "#":
      count += 1
    cur_h_idx += dx
    cur_v_idx += dy
    cur_h_idx = cur_h_idx % l_length
  return count

a = num_trees_hit(inputs, 1, 1)
b = num_trees_hit(inputs, 3, 1)
c = num_trees_hit(inputs, 5, 1)
d = num_trees_hit(inputs, 7, 1)
e = num_trees_hit(inputs, 1, 2)


print(a * b * c * d * e)