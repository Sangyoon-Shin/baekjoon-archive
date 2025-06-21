import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    k = input()
    arr.append((str(i + 1), k))

for i in arr:
    k = '. '.join(i)
    print(k, end='')