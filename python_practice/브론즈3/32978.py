import sys
input = sys.stdin.readline

n = int(input())
ans = set(input().split())
use = input().split()

for word in ans:
    if word not in use:
        print(word, end=' ')