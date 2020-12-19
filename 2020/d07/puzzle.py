from math import floor

# take in input and parse each string
# for each line, create a key-v in a dict
	# key = top color, v = array of possible contents
# function which checks bag and recursively checks down for if gold can be inside
# iterate and run prev function on each key in dict
# return count


def parse_line(line):
	container, contents = line.split(' contain ')
	container = container[0:-5]
	result = [container, {}]
	content_list = contents.split()
	num_contents = int(len(content_list) / 4)
	for x in range(num_contents):
		idx1, idx2 = (x * 4) + 1, (x * 4) + 2
		word1, word2 = content_list[idx1:idx2+1]
		result[1][(word1 + " " + word2)] = int(content_list[idx1 - 1])
	return result

RULES = {}
with open('input.txt','r') as f:
	for l in f:
		rule = parse_line(l)
		RULES[rule[0]] = rule[1]

def can_contain_shiny_gold(color):
	if len(RULES[color]) == 0:
		return False
	elif 'shiny gold' in RULES[color]:
		return True
	else:
		for el in RULES[color]:
			result = can_contain_shiny_gold(el)
			if result:
				return True
		return False

def num_bags(color):
	total = 1
	rule = RULES[color]
	for k in rule:
		total += (rule[k] * num_bags(k))
	return total



print(num_bags('shiny gold'))