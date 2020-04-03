n, t = map(int, input().split())
flag = True
ans = (float("inf"), -1)
l = list()
for i in range(n):
	s, d = map(int, input().split())
	curr_time = (t - s) / d
	if curr_time < 0:
		curr_time = 0
		flag = False
	elif int(curr_time) != curr_time:
		curr_time = int(curr_time) + 1
	curr_time = curr_time * d + s
	if ans[0] >  curr_time:
		ans = (curr_time, i + 1)
	l.append(curr_time)

print(ans[1])
