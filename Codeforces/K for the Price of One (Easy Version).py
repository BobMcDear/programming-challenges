from collections import defaultdict

def best_choice(m, p):
    if len(m) == 1:
        if m[0] <= p[0]:
            p[0] -= m[0]
            return [m[0]], 1
        return [], 0
    if len(m) == 2:
        if m[1] <= p[0]:
            p[0] -= m[1]
            return m, 2
        if m[0] <= p[0]:
            p[0] -= m[0]
            return [m[0]], 1
        return [], 0
    copy_p = [p[0] - m[1]]
    use_first_l, use_first_sc = best_choice(m[1:], [p[0] - m[0]])
    dont_use_l, dont_use_sc = best_choice(m[2:], copy_p)
    use_first_l = [m[0]] + use_first_l
    use_first_sc += 1
    dont_use_l = m[:2] + dont_use_l
    dont_use_sc += 2
    if copy_p[0] < 0:
        dont_use_sc = -1
    if use_first_sc > dont_use_sc:
        return use_first_l, use_first_sc
    return dont_use_l, dont_use_sc


"""t = int(input())
for _ in range(t):
    n, p, k  = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    bought = [False] * n
    m = 0
    if a[0] > p:
        print(m)
        continue
    for i in range(0, n-2):
        if bought[i]:
            continue
        if a[i+1] > p:
            if a[i] <= p:
                m += 1
            break
        
    if a[n-1] <= p and (not bought[n-2]) and (not bought[n-1]):
        m += 2
    elif a[n-2] <= p and (not bought[n-2]):
        m += 1"""
p = 2 * (10**9)
n = 10**5
a = [1] * n
already_calculated = defaultdict(lambda: ())
print(best_choice(a, [p]))