with open('input.txt', 'r') as f:
    input_string = f.read().replace('\n\n','&').replace(' ',',').replace('\n',',')
    inputs = map(lambda x: x.split(','), input_string.split('&'))

EYE_COLORS = {'amb','blu','brn','gry','grn','hzl','oth'}

def valid_byr(byr):
  return True if int(byr) in range(1920, 2003) else False

def valid_iyr(iyr):
  return True if int(iyr) in range(2010,2021) else False

def valid_eyr(eyr):
  return True if int(eyr) in range(2020,2031) else False

def valid_hgt(hgt):
  if hgt[-2:] == 'in':
    return True if int(hgt[:-2]) in range(59,77) else False
  elif hgt[-2:] == 'cm':
    return True if int(hgt[:-2]) in range(150, 194) else False
  else:
    return False

def valid_hcl(hcl):
  if len(hcl) != 7:
    return False
  elif hcl[0] != '#':
    return False
  else:
    for char in hcl[1:]:
      if char not in '0123456789abcdef':
        return False
    return True

def valid_ecl(ecl):
  return True if ecl in EYE_COLORS else False 

def valid_pid(pid):
  if len(pid) != 9:
    return False
  else:
    for char in pid:
      if char not in '0123456789':
        return False
    return True




def validate(pp):
  if len(pp) == 8:
    pass
  elif len(pp) < 7:
    return False
  elif len(pp) == 7 and 'cid' in map(lambda x: x[:3], pp):
    return False
  
  passport = {}
  for el in pp:
    passport[el[:3]] = el[4:]
  
  byr = passport['byr']
  iyr = passport['iyr']
  eyr = passport['eyr']
  hgt = passport['hgt']
  hcl = passport['hcl']
  ecl = passport['ecl']
  pid = passport['pid']

  if not valid_byr(byr):
    return False
  elif not valid_iyr(iyr):
    return False
  elif not valid_eyr(eyr):
    return False
  elif not valid_hgt(hgt):
    return False
  elif not valid_hcl(hcl):
    return False
  elif not valid_ecl(ecl):
    return False
  elif not valid_pid(pid):
    return False
  else:
    return True
  
count = 0
for passport in inputs:
  if validate(passport):
    count += 1

print(count)