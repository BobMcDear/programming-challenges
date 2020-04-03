from sys import exit

s = input()
if set(s) == set([')']) or set(s) == set(['(']):
    print(0)
    exit(0)
for i in range(1, len(s)):
    if set(s[:i]) == set([')']) and set(s[i:]) == set(['(']):
        print(0)
        exit(0)

c = len(s) - 1
num_open = s.count('(')
num_close = s.count(')')
num_open_copy = num_open
num_close_copy = num_close
delete = []
opens = []
closes = []
for i in range(len(s)):
    if s[i] == '(':
        opens.append(i)
for i in range(len(s)-1, -1, -1):
    if s[i] == ')':
        closes.append(i)

for i in range(min(num_open_copy, num_close_copy)):
    if opens[i] > closes[i]:
        continue
    delete.append(opens[i])
    delete.append(closes[i])
delete.sort()
print(1)
print(len(delete))
for i in delete:
    print(i+1, end=' ')
print()