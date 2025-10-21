from itertools import combinations
n = int(input())
seq = [0 for i in range(n)]
cnt = 0 
for c in combinations(seq, 4):
    cnt += 1

print(cnt)