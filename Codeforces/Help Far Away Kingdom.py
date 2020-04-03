n = input()
integer, frac = n.split('.')
if integer[len(integer) - 1] == '9':
    print("GOTO Vasilisa.")
else:
    if frac[0] < '5':
        print(integer)
    else:
        print(int(integer) + 1)