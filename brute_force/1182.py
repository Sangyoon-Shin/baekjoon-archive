import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

# 지금의 나를 포함하고 가냐, 버리고 가냐로 모두 탐색
def dfs(i, total):
    global cnt
    if i == n:
        if total == s:
            cnt += 1
        return
    else:
        dfs(i + 1, total + arr[i])
        dfs(i + 1, total)

dfs(0, 0)

if s == 0: # s가 0이면 아무것도 선택안했을 경우에 합이 0인데 이게 잡히니까 빼줘야함
    cnt -= 1
print(cnt)
    
