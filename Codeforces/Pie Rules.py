n = int(input())
p = list(map(int, input().split()))
sums = {}
a = [0] * (n+1)
b = [0] * (n+1)
a[n-1] = p[n-1]
b[n-1] = p[n-1]
for i in range(n):
    sums[i] = sum(p[i:])
for i in range(n-2, -1, -1):
    b[i] = max(p[i] + sums[i+1] - a[i+1], b[i+1])
    a[i] = max(p[i] + sums[i+1] - b[i+1], a[i+1])
print(sums[0] - b[0], b[0])