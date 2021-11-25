SUM = 0

def calc_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel <= 0: return 0
    return fuel + calc_fuel(fuel)

with open('input.txt') as f:
    for l in f:
        SUM += calc_fuel(int(l))

print(SUM)