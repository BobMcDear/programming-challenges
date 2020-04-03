n = int(input())
mn = {frozenset('A'): float('inf'), frozenset('B'): float('inf'), frozenset('C'): float('inf'), frozenset('AB'): float('inf'), frozenset('AC'): float('inf'), frozenset('BC'): float('inf'), frozenset('ABC'): float('inf')}
for _ in range(n):
    c, s = map(str, input().split())
    c = int(c)
    s = frozenset(s)
    if mn[s] > c:
        mn[s] = c
ans = min(mn[frozenset('A')]+mn[frozenset('B')]+mn[frozenset('C')], mn[frozenset('AB')]+mn[frozenset('C')], mn[frozenset('AC')]+mn[frozenset('B')], mn[frozenset('BC')]+mn[frozenset('A')], mn[frozenset('ABC')], mn[frozenset('AB')]+mn[frozenset('BC')],mn[frozenset('AB')]+mn[frozenset('AC')], mn[frozenset('AC')]+mn[frozenset('BC')])
if ans == float('inf'):
    ans = -1
print(ans)