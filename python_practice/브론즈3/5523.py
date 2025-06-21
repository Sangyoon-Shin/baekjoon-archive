import sys
input = sys.stdin.readline

awin, bwin = 0, 0
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a > b: 
        awin += 1
    elif a < b:
        bwin += 1

print(awin, bwin)
    