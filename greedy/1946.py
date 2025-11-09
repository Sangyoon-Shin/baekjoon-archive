import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    candidate = []
    for j in range(n):
        doc, interview = map(int, input().split())
        candidate.append((doc, interview))
    candidate.sort()
    cnt = 1 
    standartinterview = candidate[0][1]
    for k in range(1, len(candidate)):
        if candidate[k][1] < standartinterview:
            standartinterview = candidate[k][1]
            cnt += 1
    print(cnt)
