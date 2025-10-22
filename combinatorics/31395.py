import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

# 0번 idx부터 오름차순으로 이루어진 구간의 길이를 먼저 세고
# 만약에 오름차순이 끊기는 구간이 생기면 그때까지의 길이를 기반으로 cnt * (cnt + 1) // 2를 해준다.
# i번째부터 j번째까지 고를 수 있는 조합의 수가 cnt * (cnt + 1) // 2
cnt = 1
total = 0

for i in range(1, n):
    if seq[i - 1] < seq[i]:
        cnt += 1
    else:
        total += cnt * (cnt + 1) // 2
        cnt = 1

total += cnt * (cnt + 1) // 2
print(total)

