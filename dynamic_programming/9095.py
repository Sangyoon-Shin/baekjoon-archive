import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    # 점화식: dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
    # why? n을 만들 수 있는 가짓수는 n - 1에서 1을 더하거나, n - 2에서 2를 더하거나, n - 3에서 3을 더하는 경우가 있다.
    dp = [0] * (n + 1)
    for j in range(1, n + 1):
        if j == 1:
            dp[j] = 1
        elif j == 2:
            dp[j] = 2
        elif j == 3:
            dp[j] = 4
        else:
            dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]
        
    print(dp[n])

    
