import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = list(map(int, input().split()))
    scoresum = sum(k[1:])
    avg = scoresum / k[0]
    cnt = 0
    for j in range(1, k[0] + 1):
        if k[j] > avg:
            cnt += 1
    
    print((cnt / k[0]) * 100, end='')
    print('%')


