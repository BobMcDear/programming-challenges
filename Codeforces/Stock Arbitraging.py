n, m, r = map(int, input().split())
buy = sorted(list(map(int, input().split())))
sell = sorted(list(map(int, input().split())))
p = sell[-1] - buy[0]
if p <= 0:
    print(r)
else:
    print(sell[-1] * (r // buy[0]) + (r % buy[0]))