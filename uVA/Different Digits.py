def noRepeats(s):
    letters = set(s)
    if len(letters) == len(s):
        return True
    return False

while True:
    try:
        n, m = map(int, input().split())
        r = 0
        for i in range(n, m + 1):
            if noRepeats(str(i)):
                r += 1
        print(r)
    except EOFError:
        break