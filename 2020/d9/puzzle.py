inputs = []

with open('input.txt','r') as f:
	for l in f:
		inputs.append(int(l))


# code for p1 and sum_to_find in p2
# def two_sum(arr, targ):
# 	for el1 in arr:
# 		for el2 in arr:
# 			if el1 != el2 and (el1 + el2) == targ:
# 				return True
# 	return False
# start = 0
# end = 24
# for i, el in enumerate(inputs[25:]):
# 	result = two_sum(inputs[start:(end+1)],el)
# 	if not result:
# 		print(el)
# 	start += 1
# 	end += 1

sum_to_find = 10884537

for i, el1 in enumerate(inputs):
	end_input = 0
	current_sum = sum(inputs[i:end_input])
	while current_sum < sum_to_find:
		end_input += 1
		current_sum = sum(inputs[i:end_input])
	if current_sum == sum_to_find:
		input_range = [i, end_input]
		break

print(input_range)
start, end = input_range
x = min(inputs[start:end])
y = max(inputs[start:end])
print(x + y)