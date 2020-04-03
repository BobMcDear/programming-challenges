handles = {}
q = int(input())
for i in range(q):
    old, new = map(str, input().split())
    if old not in handles.values():
        handles[old] = new
    else:
        for j in handles:
            if handles[j] == old:
                handles[j] = new
print(len(handles))
for i in handles:
    print(i, handles[i])