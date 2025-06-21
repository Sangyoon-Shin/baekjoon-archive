import sys
input = sys.stdin.readline

info = []
n = int(input())

for i in range(n):
    name, day, month, year = map(str, input().strip().split())
    info.append((name, int(day), int(month), int(year)))

info.sort(key=lambda x: (x[3], x[2], x[1]))

for i in info:
    print(i)

print(info[len(info) - 1][0])
print(info[0][0])

