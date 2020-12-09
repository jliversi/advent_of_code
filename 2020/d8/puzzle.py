input_arr = []

with open('input.txt','r') as f:
  for l in f:
    line_arr = l.split()
    line_arr[1] = int(line_arr[1])
    input_arr.append(line_arr)


def run_program(inputs, idx_to_change):
  prev_val = inputs[idx_to_change][0]
  inputs[idx_to_change][0] = 'nop' if prev_val == 'jmp' else 'jmp'

  visited = set()
  acc = 0
  current_idx = 0
  op, arg = inputs[current_idx]
  while current_idx not in visited:
    visited.add(current_idx)
    if op == 'acc':
      acc += arg
      current_idx += 1
    elif op == 'jmp':
      current_idx += arg
    elif op == 'nop':
      current_idx +=1

    if current_idx == len(inputs):
      return acc
    op, arg = inputs[current_idx]
  
  inputs[idx_to_change][0] = prev_val
  return False

  

jmp_nop_idxs = []
for i, el in enumerate(input_arr):
  if el[0] == 'jmp' or el[0] == 'nop':
    jmp_nop_idxs.append(i)

for el in jmp_nop_idxs:
  test = run_program(input_arr, el)
  if test:
    print(test)
    break

