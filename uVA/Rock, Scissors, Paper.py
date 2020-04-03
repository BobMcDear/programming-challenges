from copy import deepcopy

combs = {('R', 'P'): 'P', ('R', 'S'): 'R', ('S', 'P'): 'S', ('P', 'R'): 'P', ('S', 'R'): 'R', ('P', 'S'): 'S', ('R', 'R'): 'R', ('S', 'S'): 'S', ('P', 'P'): 'P'}
moves = ((0, 1), (0, -1), (-1, 0), (1, 0))

def isOk(pos, r, c):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < r and pos[1] < c 

def attack(grid, r, c):
    attack_grid = deepcopy(grid)
    for i in range(r):
        for j in range(c):
            for k in moves:
                curr_pos = (i, j)
                new_pos = (i + k[0], j + k[1])
                curr_cell = grid[curr_pos[0]][curr_pos[1]]
                if not isOk(new_pos, r, c):
                    continue
                new_cell = grid[new_pos[0]][new_pos[1]]
                if combs[(new_cell, curr_cell)] == new_cell:
                    continue
                attack_grid[new_pos[0]][new_pos[1]] = combs[(curr_cell, new_cell)]
    return attack_grid

t = int(input())
for i in range(t):
    r, c, n = map(int, input().split())
    grid = [['' for i in range(c)] for j in range(r)]
    for j in range(r):
        grid[j] = list(input())
    for j in range(n):
        grid = attack(grid, r, c)
    for j in grid:
        for k in j:
            print(k, end='')
        print()
    if i < t - 1:
        print()