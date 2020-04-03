from collections import defaultdict

n, k = map(int, input().split())
s = input()
d = defaultdict(lambda: 0)
f = 0
for i in range(0, n-k+1):
    if f:
        f -= 1
        continue
    curr_chr = set()
    for j in range(i, i+k):
        curr_chr.add(s[j])
    if len(curr_chr) == 1:
        d[s[i]] += 1
        f = k
mx = 0
for i in d:
    mx = max(mx, d[i])
print(mx)