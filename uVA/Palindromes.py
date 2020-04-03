mirrors = {"A": "A", "E": "3", "H": "H", "I": "I", "J": "L", "L": "J", "M": "M", "O": "O", "S": "2", "T": "T", "U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"5","1":"1","2":"S","3":"E","5":"Z", "8":"8"}
answer = []
def isP(s):
    return s == s[::-1]

def isM(s):
    new = ''
    for i in s:
        if i not in mirrors:
            return False
        new += mirrors[i]
    return new[::-1] == s   
    
while True:
    try:
        s = input()
        p = isP(s)
        m = isM(s)
        if not p and not m:
            ans = "is not a palindrome."
        if p and not m:
            ans = "is a regular palindrome."
        if m and not p:
            ans = "is a mirrored string."
        if m and p:
            ans = "is a mirrored palindrome."
        answer.append(s + " -- {}".format(ans))

    except EOFError:
        break

for i in range(len(answer)):
    print(answer[i])
    print()