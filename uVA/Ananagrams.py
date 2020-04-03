dic = {}
ans = []
d = []
sorted_d = []
while True:
    s = input()
    if s == "#":
        break
    s = s.split()
    copy_s = s[:]
    s = [i.lower() for i in s]
    s = [''.join(sorted(i)) for i in s]
    for i in range(len(copy_s)):
        dic[s[i]] = copy_s[i]
    d += s
for i in d:
    sorted_d.append(i.lower())

for i in sorted_d:
    if sorted_d.count(i) == 1:
        ans.append(dic[i])

ans.sort()
for i in ans:
    print(i)