from sys import exit

def chert(a, b):
    for i in range(len(b)):
        if b[i] != a[i]:
            return False
    return True

alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])
s = input()
if ''.join(sorted(list(set(s)))) not in alphabet:
    print("NO")
    exit(0)

letters_so_far = ''
for i in s:
    if i not in letters_so_far:
        letters_so_far += i
if not chert(alphabet, letters_so_far):
    print("NO")
else:
    print("YES")