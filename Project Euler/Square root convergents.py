res = 0
n = 3
d = 2
for i in range(1000):
	if len(str(n)) > len(str(d)):
		res += 1
	#print('{}/{}'.format(n, d))
	# n = n + d
	n, d = 2*d+n, n+d
	# n = n + d

print(res)