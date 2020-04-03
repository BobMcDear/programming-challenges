from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
l = []
for _ in range(m):
    l.append(int(input()))
diff = {len(a):0}
diff_dict = defaultdict(lambda: False)
for i in range(len(a)-1, -1, -1):
    diff[i] = diff[i+1]
    if not diff_dict[a[i]]:
        diff[i] += 1
        diff_dict[a[i]] = True
for i in l:
    print(diff[i-1])