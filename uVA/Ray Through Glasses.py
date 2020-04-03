def fibonacci(n):
    if n - 1 in fib:
        prev1 = fib[n - 1]
    if n - 2 in fib:
        prev2 = fib[n - 2]
    

fib = {1: 1, 2: 1}
while True:
    try:
        n = int(input())
        

    except EOFError:
        break