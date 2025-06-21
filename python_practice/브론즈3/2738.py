import sys

n, m = map(int, sys.stdin.readline().split())

a = []
b = []

for i in range(n):
    value = list(map(int, sys.stdin.readline().split()))
    a.append(value)

for i in range(n):
    value = list(map(int, sys.stdin.readline().split()))
    b.append(value)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end = ' ')
    print()
