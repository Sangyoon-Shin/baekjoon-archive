import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

maximum = a//2 + b

if n >= maximum:
    print(maximum)
else:
    print(n)    