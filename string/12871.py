import sys
import math
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

lens, lent = len(s), len(t)
l = math.lcm(lens, lent)

vals, valt = l // lens, l // lent
s = s * vals
t = t * valt

if s == t:
    print(1)
else:
    print(0)
