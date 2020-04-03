t = int(input())
for i in range(t):
    n = int(input())
    num_appearance = []
    s = ''
    for j in range(1, n + 1):
        s += str(j)
    for j in range(10):
        num_appearance.append(str(s.count(str(j))))
    print(' '.join(num_appearance))