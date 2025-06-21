import sys
input = sys.stdin.readline

n, m = map(int, input().split())

saved = {}

for i in range(n):
    site, pw = map(str, input().strip().split())
    saved[site] = pw

for j in range(m):
    mysite = input().strip()
    print(saved[mysite])