from math import ceil

t = int(input())
for _ in range(t):
    n = int(input())
    a, b, c = map(int, input().split())
    s = input()
    r = [0] * n
    sc = 0
    for i in range(n):
        if s[i] == 'R' and b > 0:
            b -= 1
            r[i] = 'P'
            sc += 1
    for i in range(n):
        if s[i] == 'P' and c > 0:
            c -= 1
            r[i] = 'S'
            sc += 1
    for i in range(n):
        if s[i] == 'S' and a > 0:
            a -= 1
            r[i] = 'R'
            sc += 1
    for i in range(n):
        if r[i] == 0:
            if a > 0:
                a -= 1
                r[i] = 'R'
                continue
            if b > 0:
                b -= 1
                r[i] = 'P'
                continue
            c -= 1
            r[i] = 'S'

    if sc >= ceil(n/2):
        print('YES')
        print(''.join(r))
    else:
        print('NO')