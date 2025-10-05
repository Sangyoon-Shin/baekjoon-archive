import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

if a == 0 or b == 0:
    print("no")
elif a == 1 and b == 1:
    print("no")
else:
    print("yes")