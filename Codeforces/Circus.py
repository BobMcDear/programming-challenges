from copy import copy
n = int(input())
p = [[int(i), 0] for i in input()]

p00 = [[], []]
p01 = [[], []]
p11 = [[], []]
p10 = [[] ,[]]

indx = 0
for i, j in enumerate(list(input())):
	p[i][1] = int(j)
	if i>=n//2:
		indx = 1
	if p[i] == [0, 0]:
		p00[indx].append(i)
	if p[i] == [0, 1]:
		p01[indx].append(i)
	if p[i] == [1, 0]:
		p10[indx].append(i)
	if p[i] == [1, 1]:
		p11[indx].append(i)

s1 = len(p11[0])+len(p10[0])
s2 = len(p11[1])+len(p01[1])

flag = False
if s1 > s2:

	p00[0], p00[1] = copy(p00[1]), copy(p00[0])
	p10[0], p10[1] = copy(p10[1]), copy(p10[0])
	p01[0], p01[1] = copy(p01[1]), copy(p01[0])
	p11[0], p11[1] = copy(p11[1]), copy(p11[0])
	flag = True
	s1, s2 = s2, s1

for _ in range(6000):

	while s1 <= s2-2 and len(p00[0]) > 0 and len(p11[1]) > 0:
		p00[1].append(p00[0].pop())
		p11[0].append(p11[1].pop())
		s1 += 1
		s2 -= 1

	while s1 < s2 and len(p01[0]) > 0 and len(p11[1]) > 0: 
		p01[1].append(p01[0].pop())
		p11[0].append(p11[1].pop())
		s1 = s1+1#len(p11[0])+len(p10[0])
		#len(p11[1])+len(p01[1])
	
	while s1 < s2 and len(p10[0]) > 0 and len(p11[1]) > 0:
		p10[1].append(p10[0].pop())
		p11[0].append(p11[1].pop())
		#len(p11[0])+len(p10[0])
		s2 = s2-1#len(p11[1])+len(p01[1])
	
	while s1 < s2 and len(p00[0]) > 0 and len(p10[1]) > 0:
		p00[1].append(p00[0].pop())
		p10[0].append(p10[1].pop())
		s1 = s1+1#len(p11[0])+len(p10[0])
		#s2 = #len(p11[1])+len(p01[1])
	
	while s1 < s2 and len(p00[0]) > 0 and len(p01[1]) > 0:
		p00[1].append(p00[0].pop())	
		p01[0].append(p01[1].pop())
		#s1 = #len(p11[0])+len(p10[0])
		s2 = s2-1#len(p11[1])+len(p01[1])

#if n == 5000:
	#print(s1,s2)
if s1==s2:
	res = []
	res += p00[0]
	res += p01[0]
	res += p10[0]
	res += p11[0]
	if flag:
		chert = set(res)
		polo = [i for i in range(n)]
		polo = set(polo)
		res = list(polo - chert)

	for i in res:
		print(i + 1, end=' ')
	print()
	import sys
	sys.exit(0)

print(-1)