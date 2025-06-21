import sys
input = sys.stdin.readline

arr = [[0] * 100 for i in range(100)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for w in range(x, x + 10):
        for h in range(y, y + 10):
            if w > 100 or h > 100:
                pass
            else:
                arr[w][h] = 1

s = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            s += 1

print(s)

