import sys
input = sys.stdin.readline

cnt = {}
n = int(input())
line = list(map(int, input().split()))
for i in line:
    if i not in cnt:
        cnt[i] = 1
    else:
        if cnt[i] >= 2:
            pass
        else:
            cnt[i] += 1

total = 0
for key in cnt.keys():
    total += cnt[key]
print(total)






