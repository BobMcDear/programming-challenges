n = int(input())
strings = []
fg = True
for _ in range(n):
    strings.append(input())
strings.sort(key=len)
for i in range(n - 1):
    if len(strings[i]) == len(strings[i + 1]) and strings[i] != strings[i  + 1]:
        fg = False
        print("NO")
        break
    if len(strings[i]) < len(strings[i + 1]) and (strings[i] not in strings[i + 1]):
        fg = False
        print("NO")
        break
if fg:
    print("YES")
    for s in strings:
        print(s) 