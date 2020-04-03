t = int(input())
for i in range(t):
    p = input()
    p = sorted(p)
    h = input()
    not_in_p = []
    fl = False
    for j in range(0, len(h) - len(p)+1):
        curr_s = h[j:j+len(p)]
        curr_s = sorted(curr_s)
        if curr_s == p:
            fl = True
            break
    if fl:
        continue
    print("NO")
        
