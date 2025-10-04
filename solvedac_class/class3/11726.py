# 규칙을 찾으면 피보나치 수열과 같아짐.
# 1 2 3 5 8 ....
n = int(input())

dp = [1] * (n)

if n >= 2:
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[-1] % 10007)
