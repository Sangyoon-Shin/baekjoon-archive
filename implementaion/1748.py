import sys
input = sys.stdin.readline

n = input().rstrip()
cnt = 0

start = 1
numlen = 1
nlen = len(n)
pro = 9

# a부터 b까지 개수 => b - a + 1
while True:
    if numlen == nlen:
        cnt += (int(n) - start + 1) * nlen
        break
    else:
        cnt += pro * numlen
        numlen += 1
        pro = pro * 10
        start *= 10

print(cnt)
