n, m  = map(int, input().split())
if n == 1 or m == 1:
    print(0)
else:
    r = 0
    grid = []
    for _ in range(n):
        curr_line = list(input())
        grid.append(curr_line)
    for i in range(n - 1):
        for j in range(m - 1):
            curr_square = set()
            curr_square.add(grid[i][j])
            curr_square.add(grid[i][j+1])
            curr_square.add(grid[i+1][j])
            curr_square.add(grid[i+1][j+1])
            if curr_square == set(['f','a','c','e']):
                r += 1
    print(r)