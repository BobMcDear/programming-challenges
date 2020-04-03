def isPrime(n):
    if n == 1:
        return False
    for i in range(3, int(n ** (1/2)) + 1, +2):
        if n % i == 0:
            return False
    return True

while True:
    try:
        l, u = map(int, input().split())
        primes = []
        d = -1
        c = 1e6 + 1
        c_pair = None
        d_pair = None
        for i in range(l + ((l + 1) % 2), u + (u % 2), +2):
            if isPrime(i):
                primes.append(i)
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] > d:
                d_pair = (primes[i], primes[i + 1])
                d = primes[i + 1] - primes[i]
            if primes[i + 1] - primes[i] < c:
                c_pair = (primes[i], primes[i + 1])
                c = primes[i + 1] - primes[i]
        if c_pair:
            print("{},{} are closest, {},{} are most distant.".format(c_pair[0], c_pair[1], d_pair[0], d_pair[1]))
        else:
            print("There are no adjacent primes.")
    
    except EOFError:
        break