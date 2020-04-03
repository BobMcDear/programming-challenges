from collections import defaultdict

t = int(input())
for _ in range(t):
    f = True
    _, _ = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    a_elemnts_pos = defaultdict(lambda: [])
    for i in range(len(a)):
        a_elemnts_pos[a[i]].append(i)
    sorted_a = sorted(a_elemnts_pos)
    c = 0
    for i in sorted_a:
        curr = a_elemnts_pos[i]
        for j in curr:
            a[j] = c
            c += 1
    a_elemnts_pos = defaultdict(lambda: -1)
    for i in range(len(a)):
        a_elemnts_pos[a[i]] = i
    in_p = defaultdict(lambda: False)
    for i in p:
        in_p[i-1] = True
    f = True
    #print(a_elemnts_pos)
    for i in sorted(a_elemnts_pos):
        if i == a_elemnts_pos[i]:
            continue
        pos = a_elemnts_pos[i]
        for j in range(pos-1, i-1, -1):
            if not in_p[j]:
                print('No')
                f = False
                break
            a_elemnts_pos[a[j]] += 1
            a[j], a[j+1] = a[j+1], a[j]
        if not f:
            break
    if f:
        print('Yes')