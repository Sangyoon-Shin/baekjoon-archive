import sys
input = sys.stdin.readline

n = int(input())
info = list(map(int, input().split()))
idx = 0 
for i in range(n):
    if info[i] == -1:
        idx = i

print(min(info[:idx]) + min(info[idx + 1:]))