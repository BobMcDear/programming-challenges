n = int(input())
for _ in range(n):
    s = input() 
    t = input()
    s_keys = []
    s_values = []
    t_keys = []
    t_values = []
    i = 0
    while i < len(s): 
        same = 0
        j = i 
        while s[i] == s[j]:
            same += 1
            j += 1
            if j == len(s):
                break
        s_keys.append(s[i])
        s_values.append(same)
        i = j
        if i >= len(s):
            break
    i = 0
    while i < len(t): 
        same = 0
        j = i 
        while t[i] == t[j]:
            same += 1
            j += 1
            if j == len(t):
                break
        t_keys.append(t[i])
        t_values.append(same)
        i = j
        if i >= len(t):
            break
    if len(s_keys) != len(t_keys):
        print("NO")
        continue
    f = True
    """print(s_keys)
    print(s_values)
    print(t_keys)
    print(t_values)"""
    for i in range(len(s_keys)):
        if s_keys[i] != t_keys[i] or s_values[i] > t_values[i]:
            print("NO")
            f = False
            break
    if f:
        print("YES")