import sys
input = sys.stdin.readline

p, n = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
seq.sort()

for i in range(len(seq)):
    if p >= 200:
        break
    else:
        p += seq[i]
        cnt += 1

print(cnt)

