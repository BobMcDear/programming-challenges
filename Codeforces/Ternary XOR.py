def find(c, bigger):
    if bigger == 'chert':
        if c == '0':
            return '0', '0'
        elif c == '1':
            return '0', '1'
        return '1', '1'
    else:
        if c == '0':
            return '0', '0'
        elif c == '1':
            return '0', '1'
        return '0', '2'

t = int(input())
for _ in range(t):
    n = int(input())
    x = input()
    a = ''
    b = ''
    bigger = 'chert'
    for i in x:
        f, s = find(i, bigger)
        if bigger == 'chert':
            a += f
            b += s
            if int(f) > int(s):
                bigger = 'a'
            elif int(s) > int(f):
                bigger = 'b'
        elif bigger == 'a':
            a += str(min(int(s), int(f)))
            b += str(max(int(s), int(f)))
        else:
            b += str(min(int(s), int(f)))
            a += str(max(int(s), int(f)))
    print(a)
    print(b)