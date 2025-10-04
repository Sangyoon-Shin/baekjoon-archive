import sys
input = sys.stdin.readline

n = int(input())
stair = []
for i in range(n):
    stair.append(int(input()))
    
total = 0
dp = [0] * (n + 1)
for j in range(1, n + 1):
    if j == 1:
        dp[1] = stair[j - 1]
        total += dp[j]
    elif j == 2:
        if stair[j - 1] + stair[j - 2] > stair[j - 1]: # 두 계단을 합친게 한 개 계단 보다 크면
            dp[2] = stair[j - 1] + stair[j - 2]
        else:
            dp[2] = stair[j - 1]
        total += dp[j]
    else:
        if stair[j - 1] + stair[j - 2] > stair[j - 1]: 
            dp[j] = stair[j - 1] + stair[j - 2]
        else:
            dp[j] = stair[j - 1]
        total += dp[j]

print(total)
            





