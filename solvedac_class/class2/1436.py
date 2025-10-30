import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
num = 666

while True:
    if cnt == n:
        break
    else:
        if '666' in str(num):
            cnt += 1
    num += 1

print(num - 1)

