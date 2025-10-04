import sys
input = sys.stdin.readline

string = list(input().strip())

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    string[a], string[b] = string[b], string[a]

print(''.join(string))