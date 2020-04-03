while True:
    try:
        s = input()
        ans = ''
        f = 0
        for i in s:
            if i == '"':
                if f % 2 == 0:
                    ans += '``'
                if f % 2 == 1:
                    ans += "''"
                f += 1
            if i != '"':
                ans += i

        print(ans)
    
    except:
        break