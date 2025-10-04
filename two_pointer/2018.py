n = int(input())
start, end = 1, 1 
res = 1
cnt = 0

while start <= n//2: # n의 절반을 넘으면 뒤에 뭘 더해도 항상 n을 초과하니까 계산할 필요가 없음
    if res < n:
        end += 1
        res += end
    elif res > n:
        res -= start
        start += 1
    else:
        cnt += 1
        res -= start
        start += 1  

print(cnt + 1) # 결과 + 자기자신 해주기





