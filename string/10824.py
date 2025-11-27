import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())

front = int(str(a) + str(b))
end = int(str(c) + str(d))
print(front + end)

