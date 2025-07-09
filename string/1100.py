import sys
input = sys.stdin.readline

arr = [[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            arr[i][j] = 'W'
        else:
            arr[i][j] = 'B'

inputarr = [[0]*8 for i in range(8)]
for i in range(8):
    k = input().strip()
    k = list(k)
    inputarr[i] = k

cnt = 0
for i in range(8):
    for j in range(8):
        if arr[i][j] == 'W' and inputarr[i][j] == 'F':
            cnt += 1
print(cnt)