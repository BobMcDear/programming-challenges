from math import gcd
def neg(n):
	return n < 0
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = {}
r = 0

for i in range(n):
	if a[i] == 0:
		if b[i] == 0:
			r += 1
		continue
	g = gcd(a[i], b[i])
	p = (abs(b[i] / g), abs(a[i] / g), neg(b[i] * a[i]))
	if p in d:
		d[p] += 1
	else:
		d[p] = 1
		
if not d:
	print(r)
else:
	print(d[max(d, key=d.get)] + r)