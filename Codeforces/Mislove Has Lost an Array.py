n, l, r = map(int, input().split())
mn = (n - l + 1) + 2 ** l - 2
mx = 2 ** (r - 1) - 1 + (2 ** (r - 1)) * (n - r + 1)
print(mn, mx)