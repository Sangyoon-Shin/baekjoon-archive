import sys
input = sys.stdin.readline

while True:
    m,n = map(int, input().split())
    if m == 0 and n == 0:
        break
    else:
        print(m + n)
