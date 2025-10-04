import sys
input = sys.stdin.readline

n = int(input())

status = {}
who = list(input().rstrip().split())
for w in who:
    status[w] = 1
for i in range(n):
    name = list(input().rstrip().split())
    for na in name:
        if na in status:
            status[na] += 1

sorteds = sorted(status.items(), key=lambda x:x[1], reverse=True)
for s in sorteds:
    print(s[0], s[1] - 1)