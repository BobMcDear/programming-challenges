n, k  = map(int, input().split())
h = list(map(int, input().split()))
mn = sum(h[:k])
curr = mn
mn_ind = 0
for i in range(k, n):
    curr -= h[i-k]
    curr += h[i]
    if curr < mn:
        mn = curr
        mn_ind = i + 1 - k
print(mn_ind + 1)