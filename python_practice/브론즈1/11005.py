import sys
input = sys.stdin.readline

numtable = {}

start = 10
for i in range(26):
    numtable[chr(65 + i)] = start + i

n, b = map(str, input().split())
number = list(map(str, n))
b = int(b)


