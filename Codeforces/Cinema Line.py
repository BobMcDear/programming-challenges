input()
a = list(map(int, input().split()))
r = [0, 0, 0]
f = True
for i in a:
    if i == 25:
        r[0] += 1
    elif i == 50:
        r[1] += 1
        if r[0] == 0:
            print("NO")
            f = False
            break
        r[0] -= 1
    else:
        r[2] += 1
        if r[1] > 0 and r[0] > 0:
            r[1] -= 1
            r[0] -= 1
        elif r[0] >= 3:
            r[0] -= 3
        else:
            f = False
            print("NO")
            break

if f:
    print("YES")