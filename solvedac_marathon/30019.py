import sys
input = sys.stdin.readline

n, m = map(int, input().split())
room = {}

for i in range(m):
    num, start, end = map(int, input().split())
    if num in room:
        if start >= room[num]:
            print("YES")
            room[num] = end
        else:
            print("NO")
    else:
        print("YES")
        room[num] = end