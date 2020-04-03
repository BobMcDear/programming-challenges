t = int(input())
for i in range(t):
    d, v, u = map(int, input().split())
    if u <= v or v == 0:
        print("Case {}: can't determine".format(i + 1))
        continue
    fastest = d / u
    shortest = d / ((u ** 2 - v ** 2) ** (1/2))
    print("Case {}: {:.3f}".format(i + 1, shortest - fastest))    