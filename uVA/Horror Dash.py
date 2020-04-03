while True:
	try:
		n = int(input())
		for i in range(n):
			a = list(map(int,input().split()))
			a.pop(0)
			print("Case {}: {}".format(i + 1, max(a)))

	except EOFError:
		break