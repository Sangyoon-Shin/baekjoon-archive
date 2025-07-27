import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
count = 0

while True:
    if total >= m: # 누적합이 m보다 크면 왼쪽 줄여서 윈도우 사이즈 줄이기
        total -= arr[start]
        start += 1
    elif end == n: # 탈출조건
        break
    else:   
        total += arr[end] # 누적합이 m보다 작으면 오른쪽 늘려주기
        end += 1

    if total == m: # 얘는 while문 도는 동안 계속 수행
        count += 1

print(count)
