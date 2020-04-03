n, k = map(int, input().split())
r = 0
chert = set([str(i) for i in range(k+1)])
for i in range(n):
    a = input()
    dig = set(a)
    if chert - dig == set():
        r += 1
print(r)