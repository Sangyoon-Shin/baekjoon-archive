import sys
input = sys.stdin.readline

n = int(input())

arr = []
sum = 0
for i in range(n - 1):
    k = int(input())
    sum = sum + (k - 1)

last = int(input())

sum = sum + last
print(sum)