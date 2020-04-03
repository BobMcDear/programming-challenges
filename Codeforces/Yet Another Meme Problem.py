t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    l = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999]
    mult = 0
    for i in l:
        if b >= i:
            mult += 1
    print(a*mult)