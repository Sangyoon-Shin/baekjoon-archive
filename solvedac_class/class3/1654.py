import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))

maximum = max(line)
# 이 값을 조정해서 그 값이 n개를 만들 수 있는 최대 길이가 되게끔 해야함
while True:
    cnt = 0
    
