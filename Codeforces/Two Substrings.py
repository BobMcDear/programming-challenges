from sys import exit

s = input()
if s.count("AB") * s.count("BA") == 0:
    print("NO")
    exit(0)
if (s.count("AB") + s.count("BA") - s.count("BAB") - s.count("ABA") >= 2):
    print("YES")
else:
    print("NO")