n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_e, a_o, b_e, b_o = 0, 0, 0, 0
for i in a:
    if i % 2 == 0:
        a_e += 1
    else:
        a_o += 1
for i in b:
    if i % 2 == 0:
        b_e += 1
    else:
        b_o += 1
print(min(a_e, b_o) + min(a_o, b_e))