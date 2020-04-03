n = int(input())
s = 0 
while n != 0:
    n -= max([int(c) for c in str(n)])
    s += 1
print(s)