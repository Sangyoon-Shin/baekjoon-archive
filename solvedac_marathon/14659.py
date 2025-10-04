import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

res = 0
peak = arr[0]
count = 0

for h in arr[1:]: # for 문 한 번 -> O(n)에 가능.
    if h < peak:          
        count += 1
        if count > res:
            res = count
    else: # 막히는 지점에서 paek값 바꿔주기. 이전의 peak보다 낮은 봉우리들은 peak보다 count가 무조건 작을 수 밖에 없으니까 신경안써도됨.         
        peak = h
        count = 0

print(res)
    