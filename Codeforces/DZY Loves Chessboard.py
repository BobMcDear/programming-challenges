adj = ((0, -1), (0, 1), (-1, 0), (1, 0))

n, m = map(int, input().split())
board = []
for i in range(n):
    row = input()
    board.append(row)
for i in range(n):
    curr_row = ''
    for j in range(m):
        if board[i][j] == '-':
            curr_row += '-'
        else:
            if (i + j) % 2 == 0:
                curr_row += 'W'
            else:
                curr_row += 'B'
    print(curr_row)