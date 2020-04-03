t = int(input())
c = 1
for i in range(t):
    l, w, h = map(int, input().split())
    if max(l, w, h) > 20:
        print("Case {}: bad".format(c))
    else:
        print("Case {}: good".format(c))
    c += 1