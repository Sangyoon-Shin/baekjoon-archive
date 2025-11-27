import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    num = list(map(int, input().split()))
    value = []
    if num[0] == 0:
        break
    else:
        for i in range(1, len(num)):
            value.append(num[i])
        for comb in combinations(value, 6):
            print(*comb)
    print()

    
        