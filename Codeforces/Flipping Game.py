n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n
for i in range(1, n):
    l[i] = l[i-1] + (a[i-1] == 1)
for i in range(n-2, -1, -1):
    r[i] = r[i+1] + (a[i+1] == 1)
mx_add = -1
total = a.count(1)
for i in range(n):
    for j in range(i, n):
        curr_add = (j - i + 1) - 2 * (total - l[i] - r[j])
        if curr_add > mx_add:
            mx_add = curr_add
print(mx_add + total)