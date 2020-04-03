q = int(input())
for _ in range(q):
    s = input()
    t = input()
    f = False
    for i in s:
        if t.count(i) != 0:
            print("YES")
            f = True
            break
    if not f:
        print("NO")