from collections import defaultdict

n = int(input())
s = input()
have = defaultdict(lambda: 0)
need = 0
for i in range(0, 2*n-2):
    if i % 2 == 1:
        continue
    have[s[i]] += 1
    nxt = s[i+1].lower()
    if have[nxt] == 0:
        need += 1
    else:
        have[nxt] -= 1
print(need)