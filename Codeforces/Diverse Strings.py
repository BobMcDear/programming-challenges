n = int(input())
ans = []
for i in range(n):
	s = input()
	s_sorted = sorted(s)
	f = True
	for j in range(len(s_sorted)-1):
		if (ord(s_sorted[j]) + 1) != ord(s_sorted[j+1]):
			ans.append("No")
			f = False
			break
	if f:
		ans.append("Yes")

for i in ans:
	print(i)