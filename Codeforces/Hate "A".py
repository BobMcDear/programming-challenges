from sys import exit

def no_As(s):
    new_s = ''
    for i in s:
        if i != 'a':
            new_s += i
    return new_s

s = input()
n = len(s)
num_a = s.count('a')
x = n - num_a
if x%2 == 1:
    print(":(")
    exit(0)
x //= 2
if x == 0:
    print(s)
    exit(0)
second_part = s[-x:]
first_part = s[:x + num_a]
if no_As(first_part) == second_part:
    print(first_part)
    exit(0)
print(":(")