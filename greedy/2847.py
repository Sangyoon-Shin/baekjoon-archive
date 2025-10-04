import sys
input = sys.stdin.readline

n = int(input())
score = []

for i in range(n):
    score.append(int(input()))

# 시작은 뒤에서 두 번째부터 해야겠다. why? 무조건 감소시켜야 하니까 항상 자기 뒤의 숫자랑 비교해서 걔보다 작아질때까지 줄이고 cnt 올리기
cnt = 0
for i in range(n - 2, -1, -1):
    compare = score[i + 1]
    while score[i] >= compare:
        score[i] -= 1
        cnt += 1

print(cnt)
    