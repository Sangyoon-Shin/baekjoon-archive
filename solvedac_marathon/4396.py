import sys
input = sys.stdin.readline

n = int(input())

flag = [[0] * n for i in range(n)]
isOpen = [[0] * n for i in range(n)]
for i in range(n):
    bomb = list(input().rstrip())
    for j in range(n):
        if bomb[j] == '*':
            flag[i][j] = 1 # 지뢰있는 곳은 1로 

for i in range(n):
    status = list(input().rstrip())
    for j in range(n):
        if status[j] == 'x':
            isOpen[i][j] = 1 # 열려있는 곳은 1로

res = [['.' for _ in range(n)] for _ in range(n)]

dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)]
for i in range(n):
    for j in range(n):
        if isOpen[i][j] == 1: # 이미 열어둔 곳이라면
            if flag[i][j] == 1: # 열려있는 곳인데, 지뢰까지 있으면 지뢰 모두 보여주기
                for x in range(n):
                    for y in range(n):
                        if flag[x][y] == 1:
                            res[x][y] = '*'
            else: # 열린 곳인데 지뢰있는 곳이 아니면, 상하좌우 대각선에 있는 폭탄 개수 세야함.
                cnt = 0
                for dx, dy in dirs:
                    if 0 <= i + dx < n and 0 <= j + dy < n and flag[i + dx][j + dy] == 1:
                        cnt += 1
                res[i][j] = str(cnt)
        else: # 열린 곳이 아니면
            pass
                
for i in range(n):
    for j in range(n):
        print(res[i][j], end='')
    print()
    
            