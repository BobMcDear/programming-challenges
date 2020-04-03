t = int(input())
for i in range(t):
    urls = []
    rel = []
    for k in range(10):
        u, r = map(str, input().split())
        r = int(r)
        urls.append(u)
        rel.append(r)
    ans = max(rel)
    print("Case #{}:".format(i + 1))
    for i in range(10):
        if rel[i] == ans:
            print(urls[i])