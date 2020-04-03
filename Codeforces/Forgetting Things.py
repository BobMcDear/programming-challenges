from sys import exit

da, db = map(int, input().split())
if db == 1 and da == 9:
    print(99, 100)
    exit(0)
if da == db:
    print(str(da)+'0', str(db)+'1')
elif da > db:
    print(-1)
# da < db
else:
    if db - da >= 2:
        print(-1)
    else:
        print(str(da)+'9', str(db)+'0') 