with open('input.txt') as f:
    INPUT = [x.split(',') for x in f]


DIRS = {
    'U': (0,1),
    'R': (1,0),
    'D': (0,-1),
    'L': (-1,0)
}

def returnPts(path):
    pts = set()
    curPt = (0,0)
    for step in path:
        dir = DIRS[step[0]]
        amt = int(step[1:])
        for _ in range(amt):
            x,y = curPt
            x += dir[0]
            y += dir[1]
            curPt = x,y
            pts.add(curPt)

    return pts

a = returnPts(INPUT[0])
b = returnPts(INPUT[1])
c = a.intersection(b)

d = min(map(lambda x: abs(x[0]) + abs(x[1]),c))

print(d)