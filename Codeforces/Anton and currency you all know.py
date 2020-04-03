from sys import exit

n = input()
for i in range(0, len(n)-1):
    if int(n[i]) % 2 == 1:
        continue
    if int(n[i]) < int(n[-1]):
        n = n[:i] + n[-1] + n[i+1:len(n)-1] + n[i]
        print(n)
        exit(0)
for i in range(len(n)-2, -1, -1):
    if int(n[i]) % 2 == 0:
        n = n[:i] + n[-1] + n[i+1:len(n)-1] + n[i]
        print(n)
        exit(0)
print(-1)