from sys import exit

def nextperm(lst):
  for i in range(len(lst) - 1, 0, -1):
    if lst[i-1] < lst[i]:
      for j in range(len(lst) - 1, i-1, -1):
        if lst[i-1] < lst[j]:
          return lst[:i-1] + lst[j:j+1] + lst[:j:-1] + lst[i-1:i] + lst[j-1:i-1:-1]

def find_poss(num_t, num_f):
    curr = '0' * num_f + '1' * num_t
    prev = 'chert'
    while curr:
        curr_poss = 0
        for i in range(len(a)):
            m = 1
            if curr[i] == '0':
                m = -1
            curr_poss += a[i] * m
        if curr_poss % 360 == 0:
            print("YES")
            exit(0)
        prev = curr
        curr = nextperm(prev)
        if curr is None or curr == prev:
            break

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
num_t = n
num_f = 0
while num_t != -1:
    find_poss(num_t, num_f)
    num_t -= 1
    num_f += 1
print("NO")