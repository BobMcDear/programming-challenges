global values, suits
values = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
suits = {'S' : 4, 'H' : 3, 'D' : 2, 'C' : 1}
values_back = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'T', 11 : 'J', 12 : 'Q', 13 : 'K', 14 : 'A'}
suits_back = {4 : 'S', 3 : 'H', 2 : 'D', 1 : 'C'}
ans = []

def convert(c):
	converted = [(values[i[0]], suits[i[1]]) for i in c]
	return converted

n = int(input())
answers = []
for i in range(n):
	cards = list(map(str, input().split()))
	converted = convert(cards)
	converted_top_bottom = converted[::-1]
	cards_top_botoom = cards[::-1]
	y = 0
	for j in range(3):
		curr_card = converted_top_bottom[25]
		if curr_card[0] <= 9:
			x = curr_card[0]
		if curr_card[0] >= 10:
			x = 10
		y += x
		#print(x)
		converted_top_bottom[25 : 26 + (10 - x)] = []
	converted = converted_top_bottom[::-1]
	#print(converted)
	#print(converted[y])
	ans = values_back[converted[y - 1][0]] + suits_back[converted[y - 1][1]]
	answers.append("Case {}: {}".format(i + 1, ans))
for i in answers:
	print(i)