import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    k = list(map(int, input().split()))
    k.sort()
    print(k[7])