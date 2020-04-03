n = int(input())
a = list(map(int, input().split()))
s = sum(a)
even = []
odd = []
for i in a:
	if i % 2 == 0:
		even.append(i)
	else:
		odd.append(i)

o_e = 0 
e_o = 0
even = sorted(even)[::-1]
odd = sorted(odd)[::-1]
e_index = 0
o_index = 0
while True:
	if len(even) - 1< e_index:
		break
	e_o += even[e_index]
	if len(odd) - 1 < o_index:
		break
	e_o += odd[o_index]
	e_index += 1
	o_index += 1
e_index = 0
o_index = 0
while True:
	if len(odd) - 1 < o_index:
		break
	o_e += odd[o_index]
	if len(even) - 1 < e_index:
		break
	o_e += even[e_index]
	e_index += 1
	o_index += 1
print(min(s - e_o, s - o_e))