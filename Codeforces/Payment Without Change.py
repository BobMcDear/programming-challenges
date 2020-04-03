q = int(input())
for i in range(q):
    n, b, a, s = map(int, input().split())
    if a * n + b < s:
        print("NO")
        continue
    k = s / a
    if k >= n:
        print("YES")
    else:
        if s % a <= b:
            print("YES")
        else:
            print("NO")