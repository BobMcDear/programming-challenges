import sys
from copy import copy

sys.setrecursionlimit(101000)

def go_to_next(graph, city, dis, already_calculated, vis):
    if graph[city] == []:
        return dis
    r = []
    for i in graph[city]:
        vis[city]
        if i in already_calculated:
            curr_dis = already_calculated[i]
        else:
            curr_dis = go_to_next(curr_graph, i, dis+1, already_calculated)
        r.append(curr_dis)
    already_calculated[city] = sum(r) / len(r)
    return already_calculated[city]

n = int(input())
graph = {}
for i in range(n):
    graph[i+1] = []
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
r = go_to_next(graph, 1, 0, {})
print(r)