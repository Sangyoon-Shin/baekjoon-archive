import sys
input = sys.stdin.readline

numtable = {}

start = 10
for i in range(26):
    numtable[chr(65 + i)] = start + i

n, b = map(str, input().split())
number = list(map(str, n))
b = int(b)

res = 0
for i in range(len(number)):
    power = len(number) - 1 - i
    if number[i] in numtable.keys():
        res += b**power * numtable[number[i]]
    else:
        res += b**power * int(number[i])

print(res)
