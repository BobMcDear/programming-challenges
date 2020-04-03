n = int(input())
d = list(map(int, input().split()))
a, b = map(int, input().split())
print(sum(d[a - 1 : b - a]))