import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [] * n
B = [] * m
res = [] * n

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

m, n = map(int, input().split())    

for j in range(m):
    row = list(map(int, input().split()))
    B.append(row)

# A의 행과 B의 열 곱해서 더하기


