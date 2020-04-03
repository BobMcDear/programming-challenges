t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    r = 0
    if a > 0:
        a -= 1
        r += 1
    if b > 0:
        b -= 1
        r += 1
    if c > 0:
        c -= 1
        r += 1
    ab = ac = bc = False
    if max(a, b, c) == a:
        if b > 0:
            a -= 1
            b -= 1
            r += 1
            ab = True
        if a > 0 and c > 0:
            a -= 1
            c -= 1
            r += 1
            ac = True
    elif max(a, b, c) == b:
        if a > 0 and not ab:
            a -= 1
            b -=  1
            ab = True
            r += 1
        if b > 0 and c > 0:
            b -= 1
            c -= 1
            r += 1
            bc = True
    else:
        if a > 0 and not ac:
            a -= 1
            c -= 1
            r += 1
            ac = True
        if c > 0 and b > 0 and not bc:
            b -= 1
            c -= 1
            r += 1
            bc = True
    if a > 0 and b > 0 and not ab:
        r += 1
        a -= 1
        b -= 1
    if a > 0 and c > 0 and not ac:
        r += 1
        a -= 1
        c -= 1
    if b > 0 and c > 0 and not bc:
        r += 1
        b -= 1
        c -= 1
    if a>0 and b>0  and c>0:
        r += 1
    print(r)