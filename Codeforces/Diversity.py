s = input()
k = int(input())
if k > len(s):
    print("impossible")
else:
    if len(set(s)) >= k:
        print(0)
    else:
        print(k - len(set(s)))