import sys
from collections import deque
input = sys.stdin.readline

maxarr = []
book = {}
ans = []

maxvalue = 0

n = int(input())
idx = 0
for i in range(n):
    x = input().strip()
    maxarr.append(x)

for i in maxarr:
    if i in book:
        book[i] += 1
    else:
        book[i] = 1

for i in book.keys():
    if book[i] > maxvalue:
        ans.clear()
        ans.append(i)
        maxvalue = book[i]
    elif book[i] == maxvalue:
        ans.append(i)
        maxvalue = book[i]
    else:
        continue

ans.sort()
print(ans[0])


    
