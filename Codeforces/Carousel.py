from collections import defaultdict

q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    colors = [0] * len(a)
    mx_c = 0
    used = defaultdict(lambda: 'chert')
    used[0] = 0
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            colors[i] = colors[i-1]
            continue
        curr_color = colors[i-1] - 1
        if used[curr_color] != 'chert':
            colors[i] = used[curr_color]
        else:
            mx_c += 1
            used[curr_color] = mx_c
            colors[i] = mx_c
    print(used)
    if a[0] != a[-1]:
        if a[-1] == a[-2] or a[-2] == a[0]:
            curr_color = colors[0] - 1
            if used[curr_color] != 'chert':
                colors[i] = used[curr_color]
            else:
                mx_c += 1
                used[curr_color] = mx_c
                colors[i]
        else:
            colors[-1] = 2
            used = {1:1, 2:3, 4:10}
        
    print(len(used))
    for i in colors:
        print(i+1, end=' ')
    print()

"""
 [x-y-z-x] <-> k==3
 [x-y-z-x]
 [x-y-z]
 [1,2,3]
 1,2,2,3
 1 2 1 2
 [1,2,3,4,5]
 [x,y,z, x, y, z]
 1,2,1,2,1,2
 [x,y,z]
 n % 2 = 1
#  x y z g g
   1 2 1 2 2
   a b a c d a d b d e s 
   a 1 [2, 3]
   b 2 [3]
   c 1 [3]
   d 2 [3]
   e 1
   f 2
   g 1
"""