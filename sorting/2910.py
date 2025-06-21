import sys
input = sys.stdin.readline

n, v = map(int, input().split())

countdict = {}
firstidx = {}

numarr = list(map(int, input().split()))
info = []

for idx, i in enumerate(numarr):
    if i in countdict:
        countdict[i] += 1
    else:
        countdict[i] = 1
        firstidx[i] = idx

for i in range(n):
    num = numarr[i]
    info.append((num, firstidx[num], countdict[num]))

info.sort(key=lambda x:(-x[2], x[1]))

for res in info:
    print(res[0], end=' ')