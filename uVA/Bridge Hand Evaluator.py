global values, suits
values = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
suits = {'S' : 4, 'H' : 3, 'D' : 2, 'C' : 1}
suits_back = {4 : 'S', 3 : 'H', 2 : 'D', 1 : 'C'}
ans = []

def convert(c):
	converted = [(values[i[0]], suits[i[1]]) for i in c]
	return converted

def howManyInList(l, item, ind):
	r = 0
	for i in l:
		if i[ind] == item:
			r += 1
	return r

while True:
	try:
		cards = list(map(str, input().split()))
		converted = convert(cards)
		s = 0
		s += 4 * howManyInList(converted, 14, 0) + 3 * howManyInList(converted, 13, 0) + 2 * howManyInList(converted, 12, 0) + howManyInList(converted, 11, 0)
		#print("1: {}".format(s))
		for i in converted:
			if i[0] == 13:
				if howManyInList(converted, i[1], 1) == 1:
					s -= 1
			if i[0] == 12:
				if howManyInList(converted, i[1], 1) <= 2:
					s -= 1
			if i[0] == 11:
				if howManyInList(converted, i[1], 1) <= 3:
					s -= 1
		#print(s)
		other_rules = 0
		stopped = 0
		most = -1
		most_suit = "Chert"
		for i in [1, 2, 3, 4]:
			for j in converted:
				if j[1] == i:
					if j[0] == 14:
						stopped += 1
						break
					if j[0] == 13 and howManyInList(converted, i, 1) >= 2:
						stopped += 1
						break
					if j[0] == 12 and howManyInList(converted, i, 1) >= 3:
						stopped += 1
						break	
			if howManyInList(converted, i, 1) == 2:
				other_rules += 1
			if howManyInList(converted, i, 1) == 1:
				other_rules += 2
			if howManyInList(converted, i, 1) == 0:
				other_rules += 2
			if howManyInList(converted, i, 1) > most:
				most = howManyInList(converted, i, 1)
				most_suit = suits_back[i]
			if howManyInList(converted, i, 1) == most:
				if suits[suits_back[i]] > suits[most_suit]:
					most = howManyInList(converted, i, 1)
					most_suit = suits_back[i]

		if stopped == 4 and s >= 16:
			ans.append("BID NO-TRUMP")
			continue
		s += other_rules
		if s < 14:
			ans.append("PASS")
			continue
		if s >= 14:
			ans.append("BID {}".format(most_suit))

	except EOFError:
		for i in ans:
			print(i)
		break	