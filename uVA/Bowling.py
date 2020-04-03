ans = []
def score(game):
    r = 0
    game = game.split()
    num_count = 0
    for i in range(len(game)):
        if game[i] == 'X':
            game[i] = 10
        elif game[i] == '/':
            continue
        else:
            game[i] = int(game[i])
    for i in range(len(game)):
        if num_count == 20:
            break
        if game[i] == '/':
            r += 10 - game[i - 1]
            num_count += 1
        else:
            if game[i] == 10:
                num_count += 2
            else:
                num_count += 1
            r += game[i]
    num_count = 0
    for i in range(len(game)):
        if num_count == 20:
            break
        if game[i] == 10:
            num_count += 2
            r += game[i + 1]
            if game[i + 2] == '/':
                r += 10 - game[i + 1]
            else:
                r += game[i + 2]

        elif game[i] == '/':
            r += game[i + 1]
            num_count += 1
        else:
            num_count += 1
    return r

game = input()
while game != "Game Over":
    ans.append(score(game))
    game = input()
for i in ans:
    print(i)