import sys
input = sys.stdin.readline

n, m = map(int, input().split())

narr = {}
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(n):
    x = input().strip()
    narr[i + 1] = x

revnarr = {value:key for key, value in narr.items()}

for j in range(m):
    x = input().strip()
    if x[0] in num:
        x = int(x)
        print(narr[x])
    else:
        print(revnarr[x])

print(narr)
print(revnarr)

