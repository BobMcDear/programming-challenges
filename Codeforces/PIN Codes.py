q = int(input())
for i in range(q):
    n = int(input())
    pins = []
    for j in range(n):
        pins.append(input())
    changes = n - len(set(pins))
    for j in range(n):
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
        if pins.count(pins[j]) == 1:
            continue
        if pins[j][0] == "9":
            pins[j] = "0" + pins[j][1:]
        else:
            pins[j] = str(int(pins[j][0]) + 1) + pins[j][1:]
            

    print(changes)
    for j in pins:
        print(j)