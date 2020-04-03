q = int(input())
for i in range(q):
    s = input()
    x = min(s.count("R"), s.count("L"))
    y = min(s.count("U"), s.count("D"))
    if x == 0:
        if y == 0:
            print("0")
            print("")
        else:
            print("2")
            print("UD")
    elif y == 0:
        print("2")
        print("RL")
    else:
        print(2*(x+y))
        print(x*'R'+y*'D'+x*'L'+y*'U')
        