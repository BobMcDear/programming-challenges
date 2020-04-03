def swap(s, i):
    s = list(s)
    s[i], s[i+1] = s[i+1], s[i]
    return ''.join(s)

n = input()
n = n.split('e')
if len(n[0]) == 1 or n[0][1] != '.':
    print(int(n[0]) * (10 ** int(n[1])))
else:
    if n[0][0] == '0':
        n[0] = n[0][1:]
    to_right = int(n[1])
    f = False
    for i in range(len(n[0])):
        if n[0][i] == '.':
            f = True
        if not f:
            continue
        if to_right == 0:
            break
        if i == len(n[0]) - 1:
            break
        n[0] = swap(n[0], i)
        to_right -= 1
    while (to_right > 0):
        n[0] += '0'
        to_right -= 1
        n[0] = swap(n[0], i)
        i += 1
    s = n[0]
    if s[0] == '.':
        s = '0' + s
    s = s.rstrip('0').rstrip('.')
    if s[-1] == '.':
        print(s[:len(s)-1])
    else:
        print(s)