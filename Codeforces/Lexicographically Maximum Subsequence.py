from collections import defaultdict

s = input()
ltrs = defaultdict(lambda: [])
for i in range(len(s)):
    ltrs[s[i]].append(i)
go_through = sorted(ltrs)[::-1]
order = []
for i in go_through:
    order += ltrs[i]
curr = order[0]
r = ''
for i in order:
    if i < curr:
        continue
    r += s[i]
    curr = i
print(r)