import sys
import math
input = sys.stdin.readline

# 매 입력마다 새로운 소수 리스트를 만들 필요가 없지.. 입력 받은거에서 최대값을 기준으로 에라토스테네스의 체를 사용해서 만들어두면 됨.
inputlist = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        inputlist.append(n)

maximum = max(inputlist) * 2

num = [True for i in range(maximum + 1)]
num[0] = False
num[1] = False

for i in range(2, int(math.sqrt(maximum)) + 1):
    j = 2
    while True:
        if i * j >= maximum + 1:
            break
        else:
            num[i * j] = False
            j += 1

for i in inputlist:
    cnt = 0
    for k in range(i + 1, 2 * i + 1):
        if num[k]:
            cnt += 1
    print(cnt)



