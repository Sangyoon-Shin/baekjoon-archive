import sys
from collections import deque
input = sys.stdin.readline

board = []

for i in range(5):
    k = list(map(int, input().split()))
    board.append(k)

order = deque()
for i in range(5):
    k = list(map(int, input().split()))
    for j in k:
        order.append(j)

cnt = 0
while order:
    bingo = 0
    cnt += 1
    cur = order.popleft()
    for i in range(5):
        for j in range(5):
            if board[i][j] == cur:
                board[i][j] = 0

    # 가로 확인
    for i in range(5):
        rflag = 0
        for j in range(5):
            if board[i][j] != 0:
                rflag = 1
                break
        if rflag == 0:
            bingo += 1
    
    # 세로 확인
    for i in range(5):
        cflag = 0
        for j in range(5):
            if board[j][i] != 0:
                cflag = 1
                break
        if cflag == 0:
            bingo += 1
    
    # 대각선 확인
    # 좌상단 -> 우하단
    lrflag = 0
    for i in range(5):
        if board[i][i] != 0:
            lrflag = 1
            break
    if lrflag == 0:
        bingo += 1

    # 우상단 -> 좌하단
    rlflag = 0
    for i in range(5):
        if board[i][4 - i] != 0:
            rlflag = 1
            break
    if rlflag == 0:
        bingo += 1
    
    if bingo >= 3:
        print(cnt)
        break





        
        

    