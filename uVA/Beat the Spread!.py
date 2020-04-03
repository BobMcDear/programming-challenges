n = int(input())
ans = []
for i in range(n):
    s, d = map(int, input().split())
    x = (s + d) / 2
    y = (s - d) / 2
    a, b = max(x, y), min(x, y)
    if a + b == s and a - b == d and a >= 0 and b >= 0 and a == int(a) and b == int(b):
        ans.append((int(a), int(b)))
    else:
        ans.append("impossible")
for i in ans:
    if len(i) == 2:
        print(i[0], i[1])
    else:
        print(i)