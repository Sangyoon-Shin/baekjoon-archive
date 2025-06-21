import sys
input = sys.stdin.readline

n = int(input())
record = {}

for i in range(n):
    name, state = map(str, input().strip().split())
    if state == 'enter':
        record[name] = state
    elif state == 'leave':
        record.pop(name)

recordlist = list(record.keys())
recordlist.sort(reverse=True)

for i in recordlist:
    print(i)