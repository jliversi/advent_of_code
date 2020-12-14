from math import floor, ceil
from functools import reduce

nums = []
idxs = []
with open('test_input.txt') as f:
  arr = f.readline().split(',')
  for i in range(len(arr)):
    el = arr[i]
    if el != 'x':
      nums.append(int(el))
      idxs.append(i)

diffs = []
on_first = True
for el in zip(nums,idxs):
  if on_first:
    diffs.append(0)
    on_first = False 
  else:
    diffs.append(el[0] - el[1])

print(list(zip(nums,idxs)))
print(diffs)

# X mod nums[i] = idxs[i]
# X = idxs[i] (mod nums[i])


N = reduce(lambda x,y: x * y, nums)
print(N)

def mod_inverse(a,b):






# BRUTE FORCE
# avail = int(inputs[0])
# # buses_pt1 = [int(x) for x in inputs[1].split(',') if x != 'x']
# buses = [(int(x), i) for i, x in enumerate(inputs[1].split(',')) if x != 'x']

# first = buses[0][0]

# to_test = first 
# to_add = first
# found = False
# while not found:
#   found = True
#   to_test = to_test + to_add
#   for el in buses[1:]:
#     if (el[0] - (to_test % el[0]) == el[1]) and (to_add % el[0]) != 0:
#       to_add = to_add * el[0]
#     elif el[0] - (to_test % el[0]) != el[1]:
#       found = False
#       break

# print(to_test)





# 1st attempt to do it with chinese remaider theorem....
# product = 1
# for el in buses[1:]:
#   product *= el[0]
# print(buses)


# def eea(a,b):
#   old_r, r = a, b
#   old_s, s = 1, 0
#   old_t, t = 0, 1

#   while r != 0:
#     quot = old_r / r
#     old_r, r = r, (old_r - (quot * r))
#     old_s, s = s, (old_s - (quot * s))
#     old_t, t = t, (old_t - (quot * t))
#   return s

# def crt():
#   result = 0 
#   for pair in buses:
#     n = pair[0]
#     a = pair[1]
#     p = product/n
#     s = eea(n,p)
#     result += (a * s * p)
#   return result

# print(crt())


# PART 1
# sml_bus_id = None
# earliest = avail * 2
# for bus in buses:
#   factor = ceil(avail/bus)
#   leaving_time = bus * factor
#   dist = leaving_time - avail
#   if dist < (earliest - avail):
#     sml_bus_id = bus
#     earliest = leaving_time

# print(sml_bus_id * (earliest - avail))
