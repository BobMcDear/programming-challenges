from collections import defaultdict

t = int(input())
d = defaultdict(lambda: 'chert')
for _ in range(t):
    a, b, n = map(int, input().split())
    c = a ^ b
    if n % 3 == 0:
        print(a)
    elif n % 3 == 1:
        print(b)
    else:
        print(c)