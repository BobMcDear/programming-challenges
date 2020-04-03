n = int(input())
x = list(map(int, input().split()))
q = int(input())
m = []
for _ in range(q):
    m.append(int(input()))
orig_m = m[:]
x.sort()
m.sort()
num_shops = 0
c = 0
i = 0
d = {}
f = False
while i < len(x):
    if c >= len(m):
        break
    if m[c] < x[i]:
        d[m[c]] = num_shops
        c += 1
        f = True
        continue
    num_shops += 1
    i += 1
    f = False
if not f:
    for i in range(c, len(m)):
        d[m[i]] = num_shops
for i in orig_m:
    print(d[i])