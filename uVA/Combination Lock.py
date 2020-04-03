ans  = []
while True:
    p, a, b, c = map(int, input().split())
    if p + a + b + c == 0:
        break

    curr_p = p
    r = 720
    if curr_p < a:
        r += 360 - (a - curr_p) * 9
    if curr_p > a:
        r += (curr_p - a) * 9
    r += 360
    curr_p = a
    if curr_p < b:
        r += 9 * (b - curr_p)
    if curr_p > b:
        r += 360 - (curr_p - b) * 9
    curr_p = b
    if curr_p < c:
        r += 360 - (c - curr_p) * 9
    if curr_p > c:
        r += (curr_p - c) * 9

    ans.append(r)

for i in ans:
    print(i)