import sys
input = sys.stdin.readline

s, t, d = map(int, input().split())
print((d//(s*2)) * t )