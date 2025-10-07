import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
k = int(input())

for i in range(k):
    s, num = map(int, input().split())
    if s == 1:
        for j in range(n):
            if (j + 1) % num == 0:
                if seq[j] == 1:
                    seq[j] = 0
                else:
                    seq[j] = 1
    else:
        idx = num - 1
        r = 0
        while True:
            if idx + r < len(seq) and idx - r >= 0:
                if seq[idx + r] == seq[idx - r]:
                    if seq[idx + r] == 1:
                        seq[idx + r] = 0
                        seq[idx - r] = 0
                    else:
                        seq[idx + r] = 1
                        seq[idx - r] = 1
                    r += 1
                else:
                    break
            else:
                break

for i in range(0, n, 20):
    print(*seq[i:i+20])

