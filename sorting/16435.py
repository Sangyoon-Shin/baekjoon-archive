import sys
input = sys.stdin.readline

n , l = map(int, input().split())
height = list(map(int, input().split()))

height.sort()

for i in height:
    if i <= l:
        l += 1
    else:
        break

print(l)