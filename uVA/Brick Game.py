t = int(input())
c = 1
for i in range(t):
    ages = list(map(int, input().split()))
    n = ages.pop(0)
    print("Case {}: {}".format(c, ages[n // 2]))
    c += 1