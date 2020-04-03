n = int(input())
a = list(map(int, input().split()))
d = {a[n-1]: 1}
for i in range(n-2, -1, -1):
    if a[i+1] <= 2 * a[i]: d[a[i]] = d[a[i+1]] + 1
    else: d[a[i]] = 1
mx = 0
for i in d:
    if d[i] > mx: mx = d[i]
print(mx)