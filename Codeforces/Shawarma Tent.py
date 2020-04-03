def distance(a, b, x, y):
    return abs(a - x) + abs(b - y)

def one_side(p, x, y, s1, s2):
    r = 0
    for i in p:
        if distance(i[0], i[1], x, y) + 1 == i[2]:
            r += 1
    return r

n, x, y = map(int, input().split())
all_paths = {}
p = []
north = 0
west = 0
south = 0
east = 0
for i in range(n):
    p1, p2 = map(int, input().split())
    if p1 == x:
        if p2 > y:
            north += 1
        else:
            south += 1
    elif p2 == y:
        if p1 > x:
            east += 1
        else:
            west += 1
    elif p1 > x:
        east += 1
        if p2 > y:
            north += 1
        else:
            south += 1
    else:
        west += 1
        if p2 > y:
            north += 1
        else:
            south += 1

    #distance_with_school = distance(p1, p2, x, y)
    #p.append((p1, p2, distance_with_school))
"""moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
mx = -1
for i in moves:
    this_side = one_side(p, x + i[0], y + i[1], x, y)
    if this_side > mx:
        mx = this_side
        best = (x + i[0], y + i[1])
print(mx)
print(best[0], best[1])"""
print(max([north, south, east, west]))
if max([north, south, east, west]) == north:
    print(x, y + 1)
elif max([north, south, east, west]) == south:
    print(x, y - 1)
elif max([north, south, east, west]) == east:
    print(x + 1, y)
elif max([north, south, east, west]) == west:
    print(x - 1, y)