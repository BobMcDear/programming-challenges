t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    print(2 * (max(s) - min(s)))