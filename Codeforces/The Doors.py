n = int(input())
s = input().split()
right = s.count("1")
left = s.count("0")
r = 0
for i in s:
	r += 1
	if i == "0":
		left -= 1
	if i == "1":
		right -= 1
	if left == 0 or right == 0:
		print(r)
		break