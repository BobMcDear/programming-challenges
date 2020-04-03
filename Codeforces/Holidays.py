n = int(input())
w = n // 7
r = n % 7
mn = mx = 2 * w
mx += min(2, r)
mn += r==6
print(mn, mx)