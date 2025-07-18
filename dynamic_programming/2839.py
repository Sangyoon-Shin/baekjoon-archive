n = int(input())

inf = 99999

dp = [inf] * 5001

dp[3], dp[5] = 1, 1

for i in range(6, n + 1):
    dp[i] = min(dp[i - 3], dp[i- 5]) + 1

if dp[n] < inf:
    print(dp[n])
else:
    print(-1)