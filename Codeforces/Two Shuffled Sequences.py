n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
increasing = [-1]
decreasing = [1e6]
c = 0
for i in range(len(a)):
	if a[i] > increasing[len(increasing) - 1]:
		increasing.append(a[i])
		a[i] = -1

for i in a[::-1]:
	if i < decreasing[len(decreasing) - 1] and i != -1:
		decreasing.append(i)
increasing.pop(0)
decreasing.pop(0)
#print(increasing, decreasing)
if len(increasing) + len(decreasing) != n:
	print("NO")

if len(increasing) + len(decreasing) == n:
	print("YES")
	print(len(increasing))
	for i in increasing:
		print(i, end = ' ')
	print()
	print(len(decreasing))
	for i in decreasing:
		print(i, end = ' ')
	print()