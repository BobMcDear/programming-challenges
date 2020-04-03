from collections import defaultdict

n, m = map(int, input().split())
is_in_w = defaultdict(lambda: False)
has_reverse = defaultdict(lambda: 0)
is_a_pal =['']
for i in range(n):
    w = input()
    if w == w[::-1]:
        is_a_pal.append(w)
        continue
    is_in_w[w] = True
    if is_in_w[w[::-1]]:
        has_reverse[w] += 1
        is_in_w[w[::-1]] = False
        is_in_w[w] = False
use = []
pal = max(is_a_pal, key=len)
for i in has_reverse:
    for _ in range(has_reverse[i]):
        use.append(i)
if pal:
    f = -2
else:
    f = -1
use.append(pal)
for i in range(len(use)+f, -1, -1):
    use.append(use[i][::-1])
r = ''.join(use)
print(len(r))
print(r)