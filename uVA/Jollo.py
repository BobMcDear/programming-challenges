def win(l):
	r = 0
	for i in l:
		if i[1] > i[0]:
			r += 1
	return r

real_ans = []
while True:
	a, b, c, x, y = map(int, input().split())
	if a == 0:
		break

	ans = []
	worst = float("inf")
	winning_card = float("inf")
	worst_hands = []
	for i in [a, b, c]:
		for j in [x, y]:
			for k in list(set([a, b, c]) - set([i])):
				for z in list(set([x, y]) - set([j])):
					if worst >= win([(i, j), (k, z)]):
						worst_hands.append([(i, j), (k, z)])
	chert = False
	for i in worst_hands:
		f = 0
		for j in sorted(list(set([_ for _ in range(1, 53)]) - set([i[0][0], i[0][1], i[1][0], i[1][1]])))[::-1]:
			curr_hand = i + [(list(set([a, b, c]) - set([i[0][0], i[1][0]]))[0], j)]
			if f == 0 and win(curr_hand) < 2:
				real_ans.append(-1)
				chert = True
				break
				
			if win(curr_hand) >= 2:
				curr_ans = j

			f += 1
		if chert:
			break
		ans.append(curr_ans)
	if not chert:
		real_ans.append(max(ans))

for i in real_ans:
	print(i)