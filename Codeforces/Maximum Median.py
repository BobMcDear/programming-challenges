n, k = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print(a[0] + k)
else:
    a.sort()
    n = ((n - 1) // 2)
    a = a[n:]
    med = a[0]
    for i in range(0, n):
        add = min((a[i + 1] - a[i]) * (i + 1), k)
        k -= add
        med += add // (i + 1)
    med += k // (n + 1)
    print(med)

    # k = 5
    # 1 2 8
    # k = 4
    # med = 2

    # 4 // 2
    # add = 2
    # med += 1