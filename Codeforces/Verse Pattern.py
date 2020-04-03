from sys import exit

def num_vow(s):
    vow = ['a', 'e', 'o', 'i', 'u', 'y']
    r = 0
    for i in vow:
        r += s.count(i)
    return r

n = int(input())
p = list(map(int, input().split()))
f = True

for i in range(n):
    s = input()
    if num_vow(s) != p[i] and f:
        print("NO")
        f = False
if f:
    print("YES")