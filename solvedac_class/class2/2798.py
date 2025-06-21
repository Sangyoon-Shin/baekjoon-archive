import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

max = 0
flag = 0
for i in range(n - 2):
    if flag == 1:
        break
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum = 0
            sum = sum + arr[i] + arr[j] + arr[k]
            if sum > max and sum < m:
                max = sum
            elif sum > m:
                break
            elif sum == m:
                max = sum
                flag = 1
                break

print(max)