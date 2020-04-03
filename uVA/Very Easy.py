while True:
    try:
        n, a = map(int, input().split())
        r = 0
        for i in range(1, n + 1):
            r += i * (a ** i)
        print(r)
    
    except EOFError:
        break