def f(n):
    return 9 + sum(9 - int(d) for d in n[1 :])+(len(n) > 1)

n = input()
print(f(n))