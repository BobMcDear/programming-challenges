c = 1
while True:
    s = input()
    if s == "#":
        break
    elif s == "HELLO":
        lan = "ENGLISH"
    elif s == "HOLA":
        lan = "SPANISH"
    elif s == "HALLO":
        lan = "GERMAN"
    elif s == "BONJOUR":
        lan = "FRENCH"
    elif s == "CIAO":
        lan = "ITALIAN"
    elif s == "ZDRAVSTVUJTE":
        lan = "RUSSIAN"
    else:
        lan = "UNKNOWN"

    print("Case {}: {}".format(c, lan))
    c += 1