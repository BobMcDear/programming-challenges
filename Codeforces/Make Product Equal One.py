n = int(input())
a = map(int, input().split())
r = 0
k = []
zero = False
for i in a:
    if i >= 0:
        r += abs(i - 1)
        if i == 0:
            zero = True
    else:
        k.append(i)
for i in k:
    r += -1 - i
if len(k) % 2 == 1:
    if not zero:
        r += 2
print(r)