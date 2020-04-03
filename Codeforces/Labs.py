n = int(input())
l = [i for i in range(n)]
result = []
chert = [[i + n*j for i in range(n)] for j in range(n)]
for i in chert:
    curr = []
    for j in range(len(l)):
        curr.append(str(i[l[j]]+1))
        l[j] += 1
        l[j] %= n
    result.append(curr)

for i in range(n):
    print(' '.join([result[j][i] for j in range(n)]))