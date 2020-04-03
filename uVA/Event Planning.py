while True:
	try:
		cost = 9999999999
		n, b, h, w = map(int, input().split())
		for i in range(h):
			p = int(input())
			a = map(int, input().split())
			for l in a:
				if l >= n and p * n <= cost:
					cost = p * n
		if cost <= b:
			print(cost)
		else:
			print("stay home")

	except EOFError:
		break