t = int(input())
b = 0
for i in range(t):
    s = input().split()
    if len(s) == 1:
        print(b)
    else:
        b += int(s[1])
        