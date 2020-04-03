n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    rev_a = int(a[::-1])
    rev_b = int(b[::-1])
    sm = rev_a + rev_b
    print(int(str(sm)[::-1]))