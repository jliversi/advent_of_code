with open('input.txt', 'r') as f:
    input_string = f.read().replace('\n\n','&').replace(' ',',').replace('\n',',')
    inputs = map(lambda x: x.split(','), input_string.split('&'))


def calc_num_for_group1(gr):
  chars = set()
  for el in gr:
    for char in el:
      chars.add(char)
  return len(chars)

def calc_num_for_group2(gr):
  total = 0
  chars = {}
  for el in gr:
    for char in el:
      if char in chars:
        chars[char] += 1
      else:
        chars[char] = 1
  for char in chars:
    if chars[char] == len(gr):
      total += 1
  return total
  

total = 0
for group in inputs:
  total += calc_num_for_group2(group)

print(total)