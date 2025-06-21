import sys

a, b, c = map(int, sys.stdin.readline().split())

list = [a, b, c]
list.sort()

print(list[0], list[1], list[2])