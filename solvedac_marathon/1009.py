import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    val = a
    for j in range(2, b + 1):
        val = (val*a) % 10
    if val == 0:
        print(10)
    else:
        print(val)


