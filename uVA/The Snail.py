while True:
	h, u, d, f = map(int, input().split())
	if h == 0:
		break
	curr_height = 0
	days = 0
	f *= 0.01 * u
	while True:
		if u > 0:
			curr_height += u
		days += 1
		if curr_height > h:
			print("success on day {}".format(days))
			break
		curr_height -= d
		if curr_height < 0:
			print("failure on day {}".format(days))
			break
		u -= f