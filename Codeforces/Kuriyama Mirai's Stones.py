from collections import defaultdict

n = int(input())
v1 = list(map(int, input().split()))
v2 = sorted(v1)
sum_v = sum(v1)
l1, r1 = [0], [sum_v - v1[0]]
l2, r2 = [0], [sum_v - v2[0]]
for i in range(1, n):
    l1.append(l1[i-1]+v1[i-1])
    l2.append(l2[i-1]+v2[i-1])
    r1.append(r1[i-1]-v1[i])
    r2.append(r2[i-1]-v2[i])

m = int(input())
for _ in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(sum_v - l1[l-1] - r1[r-1])
    else:
        print(sum_v - l2[l-1] - r2[r-1])