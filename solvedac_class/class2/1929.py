import sys
import math
input = sys.stdin.readline

maximum = 1000000
arr = [True for i in range(maximum)]

arr[0] = False
arr[1] = False
for i in range(2, int(math.sqrt(maximum))):
    if arr[i] == True:
        j = 2
        while True:
            if i * j >= maximum:
                break
            else:
                arr[i * j] = False
                j += 1

m, n = map(int, input().split())

for i in range(m, n + 1):
    if arr[i] == True:
        print(i)


