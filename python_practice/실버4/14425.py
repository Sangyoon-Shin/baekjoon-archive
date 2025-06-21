import sys
input = sys.stdin.readline

n, m = map(int, input().split())

narr = set()
marr = []

for i in range(n):
    x = input().strip()
    narr.add(x)

for j in range(m):
    x = input().strip()
    marr.append(x)

cnt = 0
for _ in marr:
    if _ in narr:
        cnt += 1

print(cnt)


