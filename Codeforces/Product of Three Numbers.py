t = int(input())
for _ in range(t):
    n = int(input())
    factors = []
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            factors.append(i)
            n //= i
            break
    if not factors:
        print('No')
        continue
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0 and i != factors[0]:
            factors.append(i)
            n //= i
            break
    if len(factors) == 1:
        print('No')
        continue
    a, b = factors[0], factors[1]
    c = n
    if c == a or c == b:
        print('No')
        continue
    print('Yes')
    print(a, b, c)
