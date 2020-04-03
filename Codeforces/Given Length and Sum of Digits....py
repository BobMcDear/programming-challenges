m, s = map(int, input().split())
if 9*m < s or (m>1 and s==0):
    print(-1, -1)
elif m==1:
    print(s, s)
else:
    if s%9 == 0:
        big = '9' * (s//9) + '0' * (m-(s//9))
        if s//9 == m:
            small = '9' * m
        else:
            small = '1' + '0'*(m-1-(s//9)) + '8' + '9' * ((s//9) - 1)
    else:
        big = '9' * (s//9) + str(s%9) + '0' * (m - (s//9) - 1)
        small = ''
        num_9 = s//9
        r = (s%9) - 1
        num_0 = m - num_9 - 2
        if r == -1:
            small = '1' + '0'*(m-1-num_9) + '8' + '9' * (num_9 - 1)
        else:
            if num_0 == -1:
                num_0 += 1
                r += 1
                small = str(r) + '9' * num_9
            else:
                small = '1' + '0' * num_0 + str(r) + '9' * num_9

    print(small, big)