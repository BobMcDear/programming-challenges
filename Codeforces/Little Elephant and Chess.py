from sys import exit

for _ in range(8):
    curr_line = input()
    if curr_line != 'WBWBWBWB' and curr_line != 'BWBWBWBW':
        print("NO")
        exit(0)
print("YES")