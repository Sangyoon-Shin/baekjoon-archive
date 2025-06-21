import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))


s, t = 0, 0

print(max(sum(a), sum(b)))

