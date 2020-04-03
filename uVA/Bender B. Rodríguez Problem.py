while True:
	l = int(input())
	if l == 0:
		break
	d = "+x"
	b = list(map(str, input().split()))
	for i in b:
		if i == "No":
			continue

		if d == "+x":
			d = i
			continue

		if d == "-x":
			d = "+" + i[1] if i[0] == "-" else "-" + i[1]
			continue

		if d == "+y":
			if i == "+y":
				d = "-x"
			if i == "-y":
				d = "+x"
			continue

		if d == "-y":
			if i == "+y":
				d = "+x"
			if i == "-y":
				d = "-x"
			continue

		if d == "+z":
			if i == "+z":
				d = "-x"
			if i == "-z":
				d = "+x"
			continue

		if d == "-z":
			if i == "+z":
				d = "+x"
			if i == "-z":
				d = "-x"
	print(d)