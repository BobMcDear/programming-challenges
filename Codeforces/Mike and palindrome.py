s = input()
n = len(s)
k = n - 1
c = 0
for i in range(n):
    if s[i] != s[k]:
        c += 1
    k -= 1
    if i == k or k - i == 1:
        break
if c == 0:
    c += n % 2
if c == 1:
    print("YES")
else:
    print("NO")