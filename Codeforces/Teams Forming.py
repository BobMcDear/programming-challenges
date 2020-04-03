n = int(input())
res = 0
skills = []
skills = map(int, input().split())
skills = list(skills)
skills = sorted(skills)
for i in range(0, n, +2):
	res += skills[i + 1] - skills[i]
print(res)