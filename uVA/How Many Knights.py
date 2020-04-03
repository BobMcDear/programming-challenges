ans = []
while True:
	m, n = map(int, input().split())
	if m == 2 and n == 1:
		ans.append((2, m, n))
		continue
	if m == 2 and 2 <= n <= 4:
		ans.append((4, m, n))
		continue
	if m == 2:
		r = 0
		f = 0
		for i in range(n):
			if 0 <= (f % 4) <= 1:
				r += 2
			f += 1
		ans.append((r, m, n))
		continue
	if n == 2:
		r = 0
		f = 0
		for i in range(m):
			if 0 <= (f % 4) <= 1:
				r += 2
			f += 1
		ans.append((r, m, n))
		continue

	if (m == 1 or n == 1) and min(m, n) > 0:
		ans.append((max(m, n), m, n))
		continue
	if m == 0 and n == 0:
		break
	if m == 0 or n == 0:
		ans.append((0, m, n))
		continue
	if m % 2 == 0:
		if m == 2 and n % 4 != 0:
			if n % 2 == 0:
				ans.append((chert * n + 2, m, n))
				continue
			if n % 2 != 0:
				ans.append((chert * n + 1, m, n))
				continue
		chert = m / 2
		ans.append((chert * n, m, n))

	if m % 2 != 0:
		chert = m // 2 + 1
		if n % 2 == 0:
			ans.append((chert * (n / 2) + (chert - 1) * n / 2, m, n))
		if n % 2 != 0:
			ans.append((chert * ((n // 2) + 1) + (chert - 1) * (n // 2), m, n))


for i in ans:
	print("{} knights may be placed on a {} row {} column board.".format(int(i[0]), i[1], i[2]))