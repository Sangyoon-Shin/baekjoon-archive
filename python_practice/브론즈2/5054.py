import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    print((max(arr) - min(arr)) * 2)
