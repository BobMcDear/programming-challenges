n = int(input())
for i in range(n):
    s = input()
    if len(s) == 5:
        print(3)
        continue
    if (s[0] == 'o' and s[1] == 'n') or (s[0] == 'o' and s[2] == 'e') or (s[1] == 'n' and s[2] == 'e'): 
        print(1)
        continue
    print(2)