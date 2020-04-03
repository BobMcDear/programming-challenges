q = int(input())
for i in range(q):
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == l[2] or l[2] - 1 == l[0] or l[2] - 2 == l[0]:
        print(0)
    else:
        l[0] += 2
        print(2*(l[2]-l[0]))