import heapq as hq
from collections import defaultdict

n, d = map(int, input().split())
s = input()
graph = defaultdict(lambda: [])
for i in range(n):
    if s[i] == '0': continue
    for j in range(1, d+1):
        if i + j >= n: break
        if s[i+j] == '1': graph[i].append(i+j)
q = [(0, 0)]
r = []
v = set()
while q:
    curr_node = q.pop(0)
    if curr_node[0] == n-1:
        r.append(curr_node[1])
        continue
    for p in graph[curr_node[0]]:
        if p in v: continue
        q.append((p, curr_node[1] + 1))
        v.add(p)
if not r:
    r = [-1]
print(min(r))