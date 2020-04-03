global main_string
main_string = list("RGB" * 3000)

def diff(s, k):
    diffs = []
    r = 0
    copy_s = main_string[:]
    #print(copy_s[:10])
    for i in range(k):
        if s[i] != copy_s[i]:
            r += 1
    diffs.append(r)
    r = 0
    copy_s.pop(0)
    #print(copy_s[:10])
    for i in range(k):
        if s[i] != copy_s[i]:
            r += 1
    diffs.append(r)
    copy_s.pop(0)
    #print(copy_s[:10])
    r = 0
    for i in range(k):
        if s[i] != copy_s[i]:
            r += 1
    diffs.append(r)
    return min(diffs)

q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    s = input()
    ans = 999999999999
    for i in range(0, n - k +1):
        d = diff(s[i:i+k], k)
        #print(d)    
        if ans > d:
            ans = d
    print(ans)