t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    r = a[0]
    for i in range(1, n):
        if d  == 0:
            break
        if a[i] * i <= d:
            r += a[i]
            d -= a[i] * i
        else:
            r += d // i
            break
    print(r)