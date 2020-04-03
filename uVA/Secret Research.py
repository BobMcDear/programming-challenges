ans = []
t = int(input())
for i in range(t):
    n = int(input())
    if n in [1, 4, 78]:
        ans.append("+")
        continue
    if str(n)[len(str(n)) - 2 : len(str(n))] == "35":
        ans.append("-")
        continue
    if str(n)[0] == "9" and list(str(n)).pop() == "4":
        ans.append("*")
        continue
    ans.append("?")
for i in ans:
    print(i)