import sys
import math
input = sys.stdin.readline

MAXIMUM = 1000001
prime = [True for i in range(MAXIMUM)]
prime[0] = False
prime[1] = False

for i in range(2, int(math.sqrt(MAXIMUM)) + 1):
    j = 2
    while True:
        if i * j >= MAXIMUM:
            break
        else:
            prime[i * j] = False
            j += 1

def count(n):
    # p + q = n이니까 p = n - q. p 범위를 n // 2 까지만 하면 순서쌍 다 찾을 수 있네
    cnt = 0
    for p in range(2, n // 2 + 1):
        if prime[p] and prime[n - p]:
            cnt += 1
    print(cnt)

t = int(input())    

for i in range(t):
    n = int(input())
    count(n)
