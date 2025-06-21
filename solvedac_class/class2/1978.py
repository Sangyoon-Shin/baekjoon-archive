import sys
import math

n = int(input())

arr = []
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(n):
    if(arr[i] < 2): 
        pass
    else:
        flag = 1
        for j in range(2, arr[i]):
            if(arr[i] % j == 0):
                flag = 0
                break
        if(flag == 1):
            cnt += 1

print(cnt)