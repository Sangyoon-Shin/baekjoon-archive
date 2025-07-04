import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
record = {}
for i in range(n):
    chat = input().strip()
    if chat == "ENTER":
        record.clear()
    elif chat in record.keys():
        record[chat] += 1
    elif chat not in record.keys():
        record[chat] = 1
        cnt += 1

print(cnt)

