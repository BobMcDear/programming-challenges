n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
boy_array = [0] * 200
girl_array = [0] * 200
for i in a:
    boy_array[i] += 1
for i in b:
    girl_array[i] += 1
r = 0
for i in range(1, 101):
    if boy_array[i] == 0:
        continue
    for j in range(boy_array[i]):
        if girl_array[i - 1] > 0:
            girl_array[i - 1] -= 1
            r += 1
        elif girl_array[i] > 0:
            girl_array[i] -= 1
            r += 1
        elif girl_array[i + 1] > 0:
            girl_array[i + 1] -= 1
            r += 1
print(r)