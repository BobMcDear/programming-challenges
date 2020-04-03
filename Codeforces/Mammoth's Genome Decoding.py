n = int(input())
s = input()
a = s.count('A')
c = s.count('C')
g = s.count('G')
t = s.count('T')
if n % 4 != 0:
    print("===")
else:
    num_needed = n // 4
    if a > num_needed or c > num_needed or g > num_needed or t > num_needed:
        print("===")
    else:
        for i in s:
            if i != "?":
                print(i, end='')
            else:
                if a < num_needed:
                    print('A', end='')
                    a += 1
                elif c < num_needed:
                    print('C', end='')
                    c += 1
                elif g < num_needed:
                    print('G', end='')
                    g += 1
                elif t < num_needed:
                    print('T', end='')
                    t += 1
    print()