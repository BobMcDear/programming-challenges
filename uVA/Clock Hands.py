ans = []
while True:
    h, m = map(str, input().split(":"))
    h = int(h)
    m = int(m)
    if h == 0 and m == 0:
        break
    h = h * 30 + m / 2
    m *= 6
    r = h - m
    if r < 0:
        r = abs(r)
    if r >= 180:
        r = 360 - r
    ans.append(r)
for i in ans:
    print("%.3f" % i)