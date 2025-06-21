import sys
input = sys.stdin.readline

n = int(input())

# 오름차순으로 정렬. n으로 나눈 값이 줄 한 개가 버틸 수 있는 무게보다 크다면 그 값이 최대 중량. 아니면 
weight = []

for i in range(n):
    weight.append(int(input()))

weight.sort()

maximum = sum(weight) / n

if maximum 