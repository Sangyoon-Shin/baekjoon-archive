import sys
input = sys.stdin.readline

n = int(input())
string = input().strip()

idx = 0
sum = 0
r = 31
M = 1234567891
for i in string:
    cur = (ord(i) - ord('a') + 1) * r**idx
    sum = sum + cur
    idx += 1

print(sum % M)