n = int(input())
for i in range(n):
    p = int(input())
    c = 0
    while str(p) != str(p)[::-1]:
        p = p + int(str(p)[::-1])
        c += 1
    print(c, int(p))    