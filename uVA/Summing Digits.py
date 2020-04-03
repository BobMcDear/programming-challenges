def f(x):
    r = 0
    for i in x:
        r += int(i)
    return r

def g(x):
    while len(x) != 1:
        x = str(f(x))
    return x

while True:
    n = int(input())
    if n == 0:
        break
    print(g(str(n)))
    