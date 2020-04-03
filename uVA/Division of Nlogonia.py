ans = []
c = {(True, True): "NE", (True, False): "SE", (False, True): "NO", (False, False): "SO"}
while True:
    k = int(input())
    if k == 0:
        break
    origin = list(map(int, input().split()))
    for i in range(k):
        curr_point = list(map(int, input().split()))
        if curr_point[0] == origin[0] or curr_point[1] == origin[1]:
            #print("diversia")
            ans.append("divisa")
            continue
        ans.append(c[(curr_point[0] > origin[0], curr_point[1] > origin[1])])
        #print(c[(curr_point[0] > origin[0], curr_point[1] > origin[1])])
for i in ans:
    print(i)