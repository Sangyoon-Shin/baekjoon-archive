import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    print(min(num), max(num))