c = 1
while True:
    n = int(input())
    if n == 0:
        break
    l = list(map(int, input().split()))
    print("Case {}: {}".format(c, len(l) - l.count(0) - l.count(0)))
    c += 1