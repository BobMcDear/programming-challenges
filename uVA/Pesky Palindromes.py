def p(s):
    return s == s[::-1]

while True:
    try:
        s = input()
        pals = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr_s = s[i : j + 1]
                #print(curr_s)
                if p(curr_s):
                    pals.add(curr_s)
        print("The string '{}' contains {} palindromes.".format(s, len(pals)))
    
    except EOFError:
        break