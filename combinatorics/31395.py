import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

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

