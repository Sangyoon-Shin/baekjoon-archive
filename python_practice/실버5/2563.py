import sys
input = sys.stdin.readline

arr = [[0 for i in range(100)] for j in range(100)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x < 90 and y < 90:
        for j in range(10):
            arr[x + j][y + j] = 1

    elif x >= 90 and y < 90:
        for j in range(10):
            arr[x:100][y + j] = 1
    
    elif x < 90 and y >= 90:
        for j in range(10):
            arr[x + j][y:100] = 1

    elif x >= 90 and y >= 90:
        arr[x:100][y:100] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[x][j] == 1:
            cnt += 1




    