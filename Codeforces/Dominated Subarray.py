from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1 or n == len(set(a)):
        print(-1)
        continue
    so_far = defaultdict(lambda: [0, 0])
    counter = defaultdict(lambda: 0)
    distance = defaultdict(lambda: 0)
    for i in range(n):
        if counter[a[i]] >= 2:
            if distance[a[i]] >= i + 1- so_far[a[i]][1]:
                distance[a[i]] = i + 1 - so_far[a[i]][1]
                so_far[a[i]][1] = i + 1
            continue
        so_far[a[i]][counter[a[i]]] = i + 1
        counter[a[i]] += 1
        if counter[a[i]] == 2:
            distance[a[i]] = so_far[a[i]][1] - so_far[a[i]][0]
    print(min(distance.values()) + 1)