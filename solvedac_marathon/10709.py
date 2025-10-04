import sys
input = sys.stdin.readline

h, w = map(int, input().split())
status = [[-1]*w for _ in range(h)]
cloud = [list(input().strip()) for _ in range(h)]

for i in range(h):
    flag = False
    cnt = 0
    for j in range(w):
        if cloud[i][j] == 'c':
            cnt = 0 
            flag = True
            status[i][j] = 0
        elif cloud[i][j] == '.':
            if flag == False:
                pass
            else:
                cnt += 1
                status[i][j] = cnt
            
for i in range(h):
    for j in range(w):
        print(status[i][j], end = ' ')
    print()



