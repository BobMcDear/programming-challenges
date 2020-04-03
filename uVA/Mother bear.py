ans = []
while True:
    s = input()
    if s == "DONE":
        break
    s = s.lower()
    s = ''.join(s.split())
    new_s = ''
    for i in s:
        if i not in ['.',',','!','?']:
            new_s += i
    if new_s == new_s[::-1]:
        ans.append("You won’t be eaten!")
    else:
        ans.append("Uh oh..")
for i in ans:
    print(i)