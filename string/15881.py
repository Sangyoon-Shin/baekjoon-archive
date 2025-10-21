n = int(input())
seq = input().strip()

idx = 0
cnt = 0

while True:
    if idx >= len(seq) - 3:
        break
    if seq[idx] == 'p' and seq[idx + 1] == 'P' and seq[idx + 2] == 'A' and seq[idx + 3] == 'p':
        cnt += 1
        idx += 4
    else:
        idx += 1
print(cnt)