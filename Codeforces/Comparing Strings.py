def solve():
    s = input()
    t = input()
    if len(s) != len(t):
        print("NO")
        return
    r = []
    for i in range(len(s)):
        if s[i] != t[i]:
            r.append(i)
            if len(r) > 2:
                print("NO")
                return
    if len(r) == 1:
        print("NO")
        return
    elif len(r) == 2 and (s[r[0]] != t[r[1]] or s[r[1]] != t[r[0]]):
        print("NO")
        return 
    print("YES")
    

if __name__ == "__main__":
    solve()