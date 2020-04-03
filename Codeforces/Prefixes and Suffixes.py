from copy import copy
n = int(input())
def get_key(item):
	return len(item[0])
answer1 = ''
answer2 = ''
counter = 0
pre_suff = []
for i in range(2 * n - 2):
	pre_suff.append((input(), i))

sorted_pre_suff = sorted(pre_suff, key=get_key)
longest1, longest2 = sorted_pre_suff[2 * n - 4][0], sorted_pre_suff[2 * n - 3][0]
word1 = longest1 + longest2[n - 2]
word2 = longest2 + longest1[n - 2]

for i in range(0, 2 * n - 2, +2):
	curr_word = sorted_pre_suff[i][0]
	next_word = sorted_pre_suff[i + 1][0]
	if word1.startswith(curr_word) and word1.endswith(next_word):
		answer1 += 'PS'
		counter += 2
		continue
	if word1.startswith(next_word) and word1.endswith(curr_word):
		answer1 += 'SP'
		counter += 2

for i in range(0, 2 * n - 2, +2):
	curr_word = sorted_pre_suff[i][0]
	next_word = sorted_pre_suff[i + 1][0]
	if word2.startswith(curr_word) and word2.endswith(next_word):
		answer2 += 'PS'
		continue
	if word2.startswith(next_word) and word2.endswith(curr_word):
		answer2 += 'SP'

res = ['' for _ in range(2 * n - 2)]
answer = answer1 if counter == n * 2 - 2 else answer2
#print("answer {} answer 1 {} answer 2 {} counter {}".format(answer, answer1, answer2, counter))
for i in range(2 * n - 2):
	res[sorted_pre_suff[i][1]] = answer[i]

print(''.join(res))