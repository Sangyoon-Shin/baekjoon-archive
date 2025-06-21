import sys
from itertools import combinations
input = sys.stdin.readline

ans = set()

string = list(input().strip())
print(string)

newword = []
for i in range(1, len(string) + 1):
    word = list(combinations(string, i))
    for j in word:
        k = ', '.join(j)
        ans.add(k)

print(ans)

