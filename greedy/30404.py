import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sound = list(map(int, input().split()))
cnt, last = 0, 0

for i in range(len(sound)):
    if i == 0:
        last = sound[i]
    if last + k < sound[i]:
        cnt += 1
        last = sound[i]

print(cnt + 1)