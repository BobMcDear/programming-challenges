from math import floor

def f(x):
    return 0.5 * (-1 + (8*x+1)**0.5)

n = int(input())
num_children = floor(f(n))
print(num_children)
for i in range(1, num_children+1):
    if i == num_children:
        print(n - int(0.5*num_children*(num_children+1)) + num_children)
    else:
        print(i, end=' ')