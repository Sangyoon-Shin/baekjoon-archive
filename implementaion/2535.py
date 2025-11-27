import sys
input = sys.stdin.readline

n = int(input())
info = []
countrycnt = {}

for i in range(n):
    country, num, score = map(int, input().split())
    info.append((country, num, score))

info.sort(key=lambda x:-x[2])

medal = []
for i in range(len(info)):
    if len(medal) >= 3:
        break
    if info[i][0] not in countrycnt:
        countrycnt[info[i][0]] = 1
        medal.append((info[i][0], info[i][1]))
    else:
        if countrycnt[info[i][0]] < 2:
            countrycnt[info[i][0]] += 1
            medal.append((info[i][0], info[i][1]))
        else:
            pass
    
for r in medal:
    print(*r)


