t = int(input())
ans = []
for i in range(t):
    x, y, z = map(int, input().split())
    entire_job = x + y
    c_share = entire_job / 3
    a_c = x - c_share
    b_c = y - c_share
    ans.append(int(round((z / (a_c + b_c)) * a_c)))

for i in ans:
    print(i)