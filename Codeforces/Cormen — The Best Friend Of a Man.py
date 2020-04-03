n, k = map(int, input().split())
a = list(map(int, input().split()))
ch = 0
r = [a[0]]
for i in range(len(a)-1):
    curr_sum = a[i] + a[i+1]
    if curr_sum >= k:
        r.append(a[i+1])
        continue
    ch += k - curr_sum
    a[i+1] += k - curr_sum
    r.append(a[i+1])
print(ch)
for i in r:
    print(i, end=' ')
print()