t = int(input())
for i in range(t):
    n = int(input())
    n = ((n * 63) + 7492) * 5 - 498
    print(str(n)[len(str(n)) - 2])