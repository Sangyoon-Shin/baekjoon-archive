import sys
from itertools import product
input = sys.stdin.readline

color = []
dad = input().strip().split()
mom = input().strip().split()
color.extend(dad)
color.extend(mom)

res = set()
for c in product(color, color):
    res.add(c[0] + ' ' + c[1])

res = list(res)
res.sort()
for r in res:
    print(r)
