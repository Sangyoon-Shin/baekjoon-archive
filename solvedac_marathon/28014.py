import sys
input = sys.stdin.readline

n = int(input())

k = list(map(int, input().split()))
cnt = 0
for i in range(len(k) - 1):
    if k[i] > k[i + 1]:
        continue
    else:
        cnt += 1

print(cnt)

    
