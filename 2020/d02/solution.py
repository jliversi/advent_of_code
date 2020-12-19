inputs = []

with open('input.txt', 'r') as f:
  for l in f:
    inputs.append(l)

def validate(string):
  nums, char, pw = string.split()
  min, max = nums.split('-')
  char = char[0]
  count = 0
  for c in pw:
    if c == char:
      count += 1
  
  if count > int(max) or count < int(min):
    return False 
  else:
    return True

def validate2(string):
  nums, char, pw = string.split()
  nums = nums.split('-')
  idx1 = int(nums[0]) - 1
  idx2 = int(nums[1]) - 1
  char = char[0]

  c1 = pw[idx1]
  c2 = pw[idx2]

  total = 0
  if c1 == char:
    total += 1
  
  if c2 == char:
    total += 1
  
  return total == 1

total_valid = 0
for line in inputs:
  total_valid += 1 if validate2(line) else 0

print(total_valid)

# e = "1-3 a: abcde"
# f = "1-3 b: cdefg"
# g = "2-9 c: ccccccccc"

# print(validate2(e))
# print(validate2(f))
# print(validate2(g))