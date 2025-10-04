import sys
input = sys.stdin.readline

r, c = map(int, input().split())
state = [list(input().strip()) for _ in range(r)]
rank = []
realrank = []

for i in range(r):
    cnt = 0
    for j in range(1, c):
        if state[i][j] != '.':
            if cnt >= c - 3:
                pass
            else:
                rank.append((i, cnt))
            break
        else:
            cnt += 1

rank.sort(key=lambda x:(-x[1]))

# 등수 채우는 로직 작성해야한다 이제.
