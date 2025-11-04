import sys
input = sys.stdin.readline

n = int(input())
expect = []
for i in range(n):
    expect.append(int(input()))

expect.sort()
complain = 0

for i in range(len(expect)):
    complain += abs(expect[i] - (i + 1))

print(complain)