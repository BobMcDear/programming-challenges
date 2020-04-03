def choose(n):
    return (n**2 - n) // 2

n, k = map(int, input().split())
s = input()
chs = set(map(str, input().split()))
parts = []
curr_part = 0
r = 0
f = False
for i in s:
    if i in chs:
        f = False
        curr_part += 1
    else:
        parts.append(curr_part)
        curr_part = 0
        f = True
if not f:
    parts.append(curr_part)
for i in parts:
    r += choose(i) + i
print(r)