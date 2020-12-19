# for test input, looking for a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b
import re

with open('input.txt') as f:
  rls, i = f.read().split('\n\n')
  rule_strings, INPUTS = rls.split('\n'), i.split('\n')

RULES = dict()
for rl in rule_strings:
  split_rl = rl.split(':')
  RULES[int(split_rl[0])] = split_rl[1][1:].replace('"','')

rul_memo = dict()

def rule_to_re(idx,depth=0):
  if depth > 10:
    return ''
  if idx in rul_memo:
    return rul_memo[idx]
  parts = RULES[idx].split(' ')
  result = '('
  if parts[0] in ['a','b']:
    # base case for a and b rules
    result = parts[0]
  else:
    #case for when just series of rules
    for part in parts:
      if part == '|':
        result += '|'
      else:
        result += rule_to_re(int(part), depth + 1)
    result += ')'
      
  rul_memo[idx] = result 
  return result 

exp_to_match = '^' + rule_to_re(0) + '$'

# print(exp_to_match)

total = 0
for el in INPUTS:
  if re.match(exp_to_match, el):
    total += 1

print(total)