def calc_increasing(a, prev):
    r = []
    sc = 0
    for i in range(len(a)-1, -1, -1):
        r.append(min(prev, a[i]))
        sc += min(prev, a[i])
        prev = min(prev, a[i])
    return r[::-1], sc

def calc_decreasing(a, prev):
    r = []
    sc = 0
    for i in range(len(a)):
        r.append(min(prev, a[i]))
        sc += min(prev, a[i])
        prev = min(prev, a[i])
    return r, sc

n = int(input())
m = list(map(int, input().split()))
mx = -1
for curr_peak in range(n):
    before, before_score = calc_increasing(m[:curr_peak], m[curr_peak])
    after, after_score = calc_decreasing(m[curr_peak+1:], m[curr_peak])
    curr_possible = before + [m[curr_peak]] + after
    curr_score = m[curr_peak] + before_score + after_score
    if curr_score > mx:
        mx = curr_score
        r = curr_possible
for i in r:
    print(i, end=' ')
print()