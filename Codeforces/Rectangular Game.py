def divisors(n):
    divs = []
    for i in range(2, n + 1):
        if n % i == 0:
            divs.append([i, n // i])
    return divs

def solve(n, divs):
    if n == 1:
        return 1
    max_c = 0
    for i in divs:
        if solve(i[1], divisors(i[1])) > max_c:
            max_c = n + solve(i[1], divisors(i[1]))
    return max_c

for i in range(1000000000, 1000000001):
    print(solve(i, divisors(i)))