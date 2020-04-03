def operation(a, ind):
    a[ind], a[ind + 1] = a[ind + 1], a[ind]

q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    ind = 0
    for i in range(1, n):    
        mn_ind = a.index(i)
        if mn_ind == 0:
            ind = 1
            continue

        ind_2 = mn_ind
        while mn_ind > ind:
            print(' '.join([str(x) for x in a]), end=' -> ')
            operation(a, mn_ind - 1)
            print(' '.join([str(x) for x in a]))
            mn_ind -= 1
        ind = ind_2
    print(' '.join([str(ssssss) for ssssss in a]))