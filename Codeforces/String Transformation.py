s = input()
if len(s) < 26:
    print(-1)
else:
    abc = ''.join([f'{chr(i)}' for i in range(ord('a'), ord('z')+1)])
    ind = 0
    r = ''
    for i in s:
        if ind <= 25 and i <= abc[ind]:
            r += abc[ind]
            ind += 1
        else:
            r += i
    if ind == 26:
        print(r)
    else:
        print(-1)