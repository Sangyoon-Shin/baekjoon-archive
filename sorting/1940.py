# 아이디어: 정렬을 해놓고 가장 작은 값, 가장 큰 값에 각각 포인터 두고
# 두 개를 더한 값이 M 보다 크면? end 포인터를 작은 쪽으로 이동
# M 보다 작으면? start 포인터를 큰 쪽으로 이동
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
numlist = list(map(int, input().split()))

numlist.sort() 

start = 0
end = len(numlist) - 1

cnt = 0
while True:
    if start == end: # 서로 계속 좁혀오다가 만나면 탈출시켜야함
        break
    elif numlist[start] + numlist[end] == m: # 값 찾았을 땐 어디로 가야하지..
        cnt += 1
        end -= 1
    elif numlist[start] + numlist[end] > m:
        end -= 1
    elif numlist[start] + numlist[end] < m:
        start += 1

print(cnt)

        
