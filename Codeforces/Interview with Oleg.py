def is_filler(s):
    if len(s) < 3:
        return False
    if s != "ogo" + ((len(s) - 3)//2)*"go":
        return False
    return True

n = int(input())
s = input()
ln = n - 1
for _ in range(n):
    for i in range(n):
        if i + ln + 1 > n:
            ln -= 1
            break
        if is_filler(s[i:i+ln+1]):
            s = s[:i] + '***' + s[i+ln+1:]

print(s)