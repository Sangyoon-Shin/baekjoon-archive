import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[0], x[1])) # x[0]: x 좌표, x[1]: y 좌표. x축 기준으로 먼저 정렬하고 y축 기준 정렬

for i in arr:
    print(i[0], i[1])