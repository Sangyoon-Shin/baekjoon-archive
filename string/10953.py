import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    string = input().strip()
    a, b = map(int, string.split(','))
    print(a + b)

