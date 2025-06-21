import sys
input = sys.stdin.readline

cntsong, avg = map(int, input().split())

x = 0.0

while True:
    if int(x) // cntsong == avg:
        break
    x += 1

print(int(x))


