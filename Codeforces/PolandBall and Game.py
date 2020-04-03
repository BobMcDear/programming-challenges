from collections import defaultdict

n, m = map(int, input().split())
g, b = [], []
sim = 0
in_g, in_b = defaultdict(lambda: False), defaultdict(lambda: False)
for i in range(n):
    g.append(input())
    in_g[g[i]] = True
for j in range(m):
    b.append(input())
    if in_g[b[j]]:
        sim += 1
if n > m:
    print("YES")
elif m > n:
    print("NO")
else:
    if sim % 2 == 0:
        print('NO')
    else:
        print('YES')