n = int(input())
a = input()
f = list(map(int, input().split()))
ans = ''
r = 0
fa = 0
for i in a:
    r += 1
    chert = max(int(i), f[int(i) - 1])
    if chert != int(i):
        fa += 1
    ans += str(chert)
    if chert != f[int(i) - 1] and chert == int(i) and r != len(a) and fa > 0:
        #print(ans)
        ans = ans + a[len(ans):]
        break

print(ans)
