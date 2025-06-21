import sys
from math import ceil

input = sys.stdin.readline

n =  int(input())
call_list = list(map(int, input().split()))

sumY, sumM = 0, 0

for i in call_list:
    sumY = sumY + (ceil(i // 30) + 1)  * 10
    sumM = sumM + (ceil(i // 60) + 1) * 15

if(sumY < sumM):
    print('Y', str(sumY))
elif(sumY > sumM):
    print('M', str(sumM))
else:
    print('Y', 'M', str(sumY))