import sys
import math
input = sys.stdin.readline

arr = [True for i in range(10001)]
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(10000)) + 1):
    if arr[i] == True:
        j = 2
        while i*j < 10001:
            arr[i*j] = False
            j += 1

def solution(arr, m, n):
    res = []
    for k in range(m, n + 1):
        if arr[k] == True:
            res.append(k)
    if len(res) == 0:
        print(-1)
    else:
        print(sum(res))
        print(min(res))

m = int(input())
n = int(input())

solution(arr, m, n)

