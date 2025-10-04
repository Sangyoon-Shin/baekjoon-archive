# 일단 시작시간 기준으로 정렬해두고, cur을 첫 회의의 (a, b)에서 a로 주고 end를 b로 주고
# 탐색하면서 end >= a 인 다음 튜플 값들로 업데이트 해주면 되지않나?
# 근데 end == a 인 경우가 여러개일때 어떤 회의를 먼저 시키는게 좋지? 무조건 빨리 끝나는걸 줘야함. 
# 그럼 정렬 기준을 a, b 둘 다 적용해줘야 겠네

import sys
input = sys.stdin.readline

n = int(input())
time = []
for i in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x:(x[1], x[0]))
cnt = 1 # 첫 회의는 무조건 진행되니까
cur = time[0][0]
end = time[0][1]

if n == 1:
    print(1)
else:
    for i in range(1, n):
        if time[i][0] >= end:
            cur = time[i][0]
            end = time[i][1]
            cnt += 1
print(cnt)


