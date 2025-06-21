import sys
input = sys.stdin.readline

arr = []
rankboard = {}
n = int(input())

for i in range(n):
    w, h = map(int, input().split())
    arr.append((i + 1, w, h))

sortedarr = sorted(arr, key=lambda x:(x[1]))

for i in range(n):
    rank = 1
    for j in range(i + 1, n):
        if sortedarr[i][1] < sortedarr[j][1] and sortedarr[i][2] < sortedarr[j][2]:
            rank += 1
    rankboard[sortedarr[i][0]] = rank

for i in range(n):
    print(rankboard[arr[i][0]], end=' ')

    
        
 