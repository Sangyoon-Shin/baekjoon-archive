import sys
input = sys.stdin.readline

# 상자를 최소한으로 사용하려면 -> 가장 큰 박스부터 사용하자
t = int(input())
for i in range(t):
    candy, box = map(int, input().split())
    cnt = 0
    boxsize = []
    for j in range(box):
        row, col = map(int, input().split())
        boxsize.append(row*col)
    
    boxsize.sort(reverse=True)
    for k in boxsize:
        if candy <= 0:
            break
        else:
            candy -= k
            cnt += 1
    print(cnt)



