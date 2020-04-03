decimals = {}
passwrd = input()
for i in range(10):
    decimals[input()] = str(i)
ans = ''
for i in range(0, 80, 10):
    ans += decimals[passwrd[i:i+10]]
print(ans)