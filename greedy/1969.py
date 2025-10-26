import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = []
res = []
dist = 0
for i in range(n):
    dna.append(input().rstrip())

for i in range(m):
    cnt = {}
    for j in range(n):
        # 같은 열의 dna에 대해서 가장 많이 일치하는 dna로, 일치하는 dna가 여러개면 사전순으로 빠른 애로 채워주기
        if dna[j][i] not in cnt:
            cnt[dna[j][i]] = 1
        else:
            cnt[dna[j][i]] += 1
    # 나온 횟수는 내림차순, 사전순은 오름차순으로
    sortedcnt = sorted(cnt.items(), key=lambda x:(-x[1], x[0]))
    res.append(sortedcnt[0][0])
    for k in range(1, len(sortedcnt)):
        dist += sortedcnt[k][1]

print(''.join(res))
print(dist)

    
