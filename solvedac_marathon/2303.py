import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
res = []
num = []

for i in range(n):
    num.append(list(map(int, input().split())))

# 조합을 다 만들어놔야하나

for i in range(len(num)):
    val = []
    for comb in combinations(num[i], 3):
        value = str(sum(comb))
        value = int(value[-1])
        val.append(value)
    res.append((i + 1, max(val)))

res.sort(key=lambda x:(-x[1], -x[0]))
print(res[0][0])    

    











