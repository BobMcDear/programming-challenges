t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if s[0] != "<" or s[n-1] != ">":
        print(0)
    else:
        print(min(s.index(">"), n - ''.join(list(s)).rindex('<') - 1))