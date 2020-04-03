english_letters = [chr(x) for x in range(97, 123)]
n = int(input())
ans = []
for i in range(n):
	n, k = map(int, input().split())
	usable_letters = english_letters[0 : k]
	while n != 0:
		for i in usable_letters:
			if n == 0:
				break
			print(i, end = '')
			n -= 1
	print()