vowels = ['a', 'o', 'y', 'e', 'u', 'i', 'A', 'O', 'Y', 'E', 'U', 'I']
s = input()
s = list(s)
delete = []
for i in range(len(s)):
    if s[i] in vowels:
        delete.append(i)
for i in range(len(delete)):
    s.pop(delete[i])
    for j in range(len(delete)):
        delete[j] -= 1
    
s = list(''.join(s).lower())
for i in s:
    print('.'+i, end='')
print()