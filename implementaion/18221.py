import sys
input = sys.stdin.readline

n = int(input())
status = []

for i in range(n):
    row = list(map(int, input().split()))
    status.append(row)
    for j, v in enumerate(row):
        if v == 5:
            px , py = i, j
        if v == 2:
            sx, sy = i, j

dist = (px - sx) ** 2 + (py - sy) ** 2

if dist < 25:
    print(0)
else:
    x1, x2 = min(px, sx), max(px, sx)
    y1, y2 = min(py, sy), max(py, sy)

    cnt = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if status[i][j] == 1:
                cnt += 1
    if cnt >= 3:
        print(1)
    else:
        print(0)

