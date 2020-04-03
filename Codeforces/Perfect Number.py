def is_per(n):
    r = 0 
    for i in str(n):
        r += int(i)
    return r == 10

def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

n = int(input())
c = 0
for i in range(1, 10**8):
    if sum_digits3(i) == 10:
        c += 1
    if c == n:
        print(i)
        break