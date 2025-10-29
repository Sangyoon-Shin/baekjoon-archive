import sys
input = sys.stdin.readline

n = int(input())
seq = []

for i in range(n):
    a, b = map(str, input().strip().split())
    seq.append((a, b))

seq.sort(key=lambda x:x[1], reverse=True)
seq.sort(key=lambda x:x[0])

for i in seq:
    print(*i)