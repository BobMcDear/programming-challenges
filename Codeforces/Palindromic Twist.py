def is_prev_or_next(a, b):
    return abs(ord(b) - ord(a)) == 0 or abs(ord(b) - ord(a)) == 2

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    k = n - 1
    fg = True
    for j in range(0, n//2):
        if not is_prev_or_next(s[j], s[k]):
            fg = False
            break
        k -= 1
    if fg:
        print("YES")
    else:
        print("NO")
    