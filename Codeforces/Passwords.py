n, k = map(int, input().split())
less = 0
eq = 0
a = []
for _ in range(n):
    a.append(input())
s = input()
for i in a:
    if len(i) < len(s):
        less += 1
    elif len(i) == len(s):
        eq += 1
print((less+1)+(less//k)*5, (less+eq)+((less+eq-1)//k)*5)