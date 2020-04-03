t = int(input())
for i in range(t):
    x, y, a, b = map(int, input().split())
    s = a + b
    if (y-x) % s == 0:
        print((y-x)//s)
    else:
        print(-1)