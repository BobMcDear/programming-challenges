import sys

a, b, c, d = map(int, input().split())
c_a = a
c_c = c
a, c = min(a, b, c), max(a, b, c)
b = c_a + c_c + b - a - c
#print(a, b, c)
d_c = b + d - c
if d_c < 0:
    d_c = 0
a = b - a + b
d_a = b + d - a
#print(d_a, d_c)
if d_a < 0:
    d_a = 0
print(d_a + d_c)
