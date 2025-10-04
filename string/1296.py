import sys
input = sys.stdin.readline

green = input().rstrip()
n = int(input())
res = []

for i in range(n):
    name = input().rstrip()
    lc = green.count('L') + name.count('L')
    oc = green.count('O') + name.count('O')
    vc = green.count('V') + name.count('V')
    ec = green.count('E') + name.count('E')

    score = ((lc + oc) * (lc + vc) * (lc + ec) * (oc + vc) * (oc + ec) * (vc + ec)) % 100
    res.append((name, score))

res.sort(key=lambda x:(-x[1], x[0]))
print(res[0][0])