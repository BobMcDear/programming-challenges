from math import gcd
answers = []
c = 1
while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    denominator = n.pop(0)
    numerator = sum(n)
    if numerator % denominator == 0:
        sign = '' if numerator == abs(numerator) else '- '
        answers.append("Case {}:\n{}".format(c, sign + str(int(abs(numerator / denominator)))))

    else:
        sign = '' if numerator == abs(numerator) else '- '
        frac_part_num = abs(numerator) % denominator
        g = gcd(frac_part_num, denominator)
        int_part = sign + str(int(abs((abs(numerator) - (abs(numerator) % denominator)) / denominator)))
        if int_part == '0' or int_part == '- 0':
            int_part = sign
        frac_part_num = int(frac_part_num / g)
        denominator = int(denominator / g)
        hyphens = '-' * len(str(denominator))
        spaces_num = ' ' * (len(str(denominator)) - len(str(frac_part_num)) + len(str(int_part)))
        spaces_den = ' ' * (len(str(int_part)))
        answers.append("Case {}:\n{}\n{}\n{}".format(c, spaces_num + str(frac_part_num), int_part + hyphens, spaces_den + str(denominator)))
    c += 1

for i in answers:
    print(i)