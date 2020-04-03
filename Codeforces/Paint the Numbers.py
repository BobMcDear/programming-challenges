from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
r = 0
while a:
    mn = min(a)
    to_del = defaultdict(lambda: False)
    for i in range(len(a)):
        if a[i] % mn == 0:
            to_del[i] = True
    a = [i for j, i in enumerate(a) if not to_del[j]]
    r += 1
print(r)