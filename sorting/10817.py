import sys
input = sys.stdin.readline

k = list(map(int, input().split()))
k.sort()
print(k[1])