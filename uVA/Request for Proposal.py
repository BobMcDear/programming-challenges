c = 1
while True:
	names = []
	n, p = map(int, input().split())
	if n == 0 and p == 0:
		break
	for i in range(n):
		r = input()
	comps = []
	for i in range(p):
		name = input()
		price, met = map(float,input().split())
		names.append(name)
		comps.append((met,price))
		for j in range(int(met)):
			chert = input()
	mn_m = -1
	for i in comps:
		if i[0] > mn_m:
			mn_m = i[0]

	mn_p = 999999999999999999
	for i in range(len(comps)):
		if comps[i][0] == mn_m:
			if mn_p > comps[i][1]:
				mn_p = comps[i][1]
	if c != 1:
		print()
	print("RFP #{}".format(c))	
	print(names[comps.index((mn_m, mn_p))])
	c += 1