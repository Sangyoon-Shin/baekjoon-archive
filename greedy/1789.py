s = int(input())
n = 0
cnt = 0

# 일단 n은 갯수. 갯수가 최대가 되게 하려면 작은 수들 먼저 골라서 s가 되는 방향으로 가야함
while True:
    if s - n > 0:
        n += 1
        s -= n
        cnt += 1
    else:
        break

print(cnt)
