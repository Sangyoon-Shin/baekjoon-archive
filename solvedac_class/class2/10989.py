# 시간초과 -> input()
# 메모리초과 -> sort()
import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * (10001)

for i in range(n):
    a = int(input())
    arr[a] += 1

for i in range(len(arr)):
    if(arr[i] != 0):
        for j in range(arr[i]):
            print(i)
