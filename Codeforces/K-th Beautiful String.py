from math import ceil

def f(n):
    return ceil((1+(8*n+1)**0.5)*0.5)

def findNumber( n ): 
      
    n -= 1
      
    # One by one subtract counts 
    # elements in different blocks 
    i = 1
    while n >= 0: 
        n -= i 
        i += 1
    return (n + i) 
  

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = ['a'] * n
    s[f(k)-1] = 'b'
    s[findNumber(k)-1] = 'b'
    print(''.join(s[::-1]))