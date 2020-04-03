c = 1
while True:
    s = input()
    if s == "*":
        break
    if s == "Hajj":
        print("Case {}: Hajj-e-Akbar".format(c))
    if s == "Umrah":
        print("Case {}: Hajj-e-Asghar".format(c))
    c += 1