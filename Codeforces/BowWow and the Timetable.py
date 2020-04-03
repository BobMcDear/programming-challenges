from math import log
s = input()
s = int(s, 2)
if s == 0:
    print(0)   
else:
    ans = log(s) / log(4)
    if int(ans) == ans:
        print(int(ans))

    else:
        print(int(ans) + 1)