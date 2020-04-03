import sys

n = int(input())    
s = input()
if s == ''.join(sorted(s)):
    print("NO")
    sys.exit(0)
for i in range(n - 1):
    if s[i + 1] < s[i]:
        print("YES")
        print(i + 1, i + 2)
        break