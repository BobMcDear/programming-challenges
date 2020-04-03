from copy import copy

n, k = map(int, input().split())
t = input()
to_print = copy(t)
for i in range(1, n):
    if t[i:] == t[:n-i]:
        to_print = t[n-i:]
        break
t += (k-1) * to_print
print(t)