from sys import exit

n = int(input())
s = input()
for i in range(n - 1):
    if s[i] != s[i+1]:
        print("YES")
        print(s[i:i+2])
        exit(0)
print("NO")