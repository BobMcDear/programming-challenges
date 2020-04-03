def chert(s):
    new = [s[0]]
    for i in range(1, len(s)):
        if s[i-1]=='A':
            new.append('A')
        else:
            new.append(s[i])
    return list(new)
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    ans = 0
    prev = s[:]
    while True:
        s=chert(s)
        if s == prev:
            break
        ans += 1
        prev = s
    print(ans)
