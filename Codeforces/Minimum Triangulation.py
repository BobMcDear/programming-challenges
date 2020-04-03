n = int(input())
d = [6]
for i in range(1, 500):
    d.append(d[i-1] + (i+3)*(i+2))
print(d[n-3])