from sys import exit
h, n = map(int, input().split())
h1 = h
d = list(map(int, input().split()))
sm = sum(d)
mn = 1e12
c = 0
ind = 0
for i in range(len(d)):
	c += d[i]
	if mn > c:
		mn = c
		ind = i + 1

c = 0
for i in d:
	h1 += i
	c += 1
	if h1 <= 0:
		print(c)
		exit(0)

if h1 >= h:
	print(-1)
	exit(0)

r = (h + mn) // -sm
h -= r * abs(sm)
c = 0
while True:
	for i in d:
		if h <= 0:
			print(c + r * n)
			exit(0)
		h += i
		c += 1