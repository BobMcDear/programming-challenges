def next_letter(l):
    if l == 'z':
        return 'a'
    return chr(ord(l) + 1)

n = int(input())
s = input()
if n > 26:
    print(-1)
else:
    print(n - len(set(list(s))))