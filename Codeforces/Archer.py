a, b, c, d = map(int, input().split())
n = 10**6
s = a/b
prev_term = a/b
for i in range(n):
    prev_term *= ((b-a)/b) * ((d-c)/d)
    s += prev_term
print(s)