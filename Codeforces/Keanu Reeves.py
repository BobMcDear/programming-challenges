def good(s):
    return s.count('1') != s.count('0')

n = int(input())
s = input()
if good(s):
    print(1)
    print(s)
else:
    for i in range(1, len(s)):
        curr_s = s[0 : i]
        next_s = s[i :]
        if good(curr_s) and good(next_s):
            print(2)
            print(curr_s, next_s)
            break