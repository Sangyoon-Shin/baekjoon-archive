import sys
input = sys.stdin.readline

a, b = map(int, input().split())

res = (min(a//2, b))
print(res)