with open('input.txt') as f:
  INPUTS = [l.replace('\n', '') for l in f]

def solve2(eq_str):
  if len(eq_str) == 1:
    return eq_str
  
  num_parens = 0
  sub_eq = ''

  terms = []

  for char in eq_str:
    # ignore spaces
    if char == ' ':
      pass

    # case when in parens
    elif num_parens > 0:
      if char == ')' and num_parens == 1:
        terms.append(sub_eq)
        sub_eq = ''
        num_parens -= 1
        continue
      sub_eq += char 
      if char == '(':
        num_parens += 1
      elif char == ')':
        num_parens -= 1
    elif char == '(':
      num_parens += 1
    else:
      terms.append(char)

  new_eq_str = ''.join([str(solve2(x)) for x in terms])
  result = 1
  for eq in new_eq_str.split('*'):
    term = 0
    for el in eq.split('+'):
      term += int(el)
    result *= term
  
  return result


print(sum([solve2(x) for x in INPUTS]))












# def solve(eq_str):
#   if eq_str[0].isnumeric():
#     result = int(eq_str[0])
#     mode = None
#     num_parens = 0
#   else:
#     result = 0
#     mode = '+'
#     num_parens = 1
#   sub_eq = ''
#   for char in eq_str[1:]:
#     # ignore spaces
#     if char == ' ':
#       pass
#     # case when in parens
#     elif num_parens > 0:
#       if char == ')' and num_parens == 1:
#         sub_result = solve(sub_eq)
#         sub_eq = ''
#         result = run_eq(result, mode, sub_result)
#         mode = None
#         num_parens -= 1
#         continue
#       sub_eq += char 
#       if char == '(':
#         num_parens += 1
#       elif char == ')':
#         num_parens -= 1
#     elif char.isnumeric():
#       result = run_eq(result, mode, int(char))
#       mode = None
#     elif char == '(':
#       num_parens += 1
#     elif char == '+':
#       mode = '+'
#     elif char == '*':
#       mode = '*'
#   return result
# def run_eq(num1, op, num2):
#   if op == '+':
#     return num1 + num2
#   else:
#     return num1 * num2

# print(sum([solve(x) for x in INPUTS]))