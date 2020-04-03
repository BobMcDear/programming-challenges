t = int(input())
c = 1
for i in range(t):
    x, y, z = map(int, input().split())
    print("Case {}: {}".format(c, sorted([x, y, z])[1]))
    c += 1