def isOk(a, n):
    if a[0] >= a[n - 1] + a[1] or a[n - 1] >= a[0] + a[n - 2]:
        return False
    for i in range(1, n - 1):
        if a[i] >= a[i - 1] + a[i + 1]:
            return False
    return True

def opposite(n, p):
    if n % 2 == 1 and p == n // 2 + 1:
        return p
    return n - p

n = int(input())
a = list(map(int, input().split()))
a.sort()
perm = a[:]
stack = [(x, opposite(n, x + 1)) for x in range(n//2)]
for i in range(n // 2):
    perm[i], perm[i + n // 2] = a[stack[i][0]], a[stack[i][1]]
if n % 2 != 0:
    perm[n - 1] = a[n // 2]
"""if n % 2 != 0:
    stack.append((a[n // 2], a[n // 2]))"""

f = True
while not isOk(perm, n):
    if not stack:
        print("NO")
        f = False
        break
    curr_nums = stack.pop()
    perm[curr_nums[0]], perm[curr_nums[1]] = perm[curr_nums[1]], perm[curr_nums[0]]

if f:
    print("YES")
    for i in range(n):
        print(perm[i], end='')
        if i < n - 1:
            print(' ', end='')
    print()