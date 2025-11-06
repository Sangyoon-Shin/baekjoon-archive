import sys
input = sys.stdin.readline

n = int(input())
info = []

for i in range(n):
    info.append(tuple(map(int, input().split())))

info.sort(key=lambda x:(x[0], x[1]))

start = info[0][0] + info[0][1]

for i in range(1, len(info)):
    # 앞에가 끝나는 시간보다 시작 시간이 빠르면? 대기
    # 앞에가 끝나는 시간과 같거나 느리면? 바로 시작
    if start > info[i][0]:
        start += info[i][1]
    else:
        start = info[i][0] + info[i][1]
    
print(start)
