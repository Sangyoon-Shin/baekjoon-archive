import sys
input = sys.stdin.readline

n = int(input())

num = []
ans = []
num_cnt = {}

for i in range(n):
    x = input().strip()
    num.append(x)

for i in num:
    if i in num_cnt:
        num_cnt[i] += 1
    else:
        num_cnt[i] = 1

maxvalue = 0

for i in num_cnt.keys():
    if num_cnt[i] > maxvalue:
        ans.clear()
        ans.append(int(i))
        maxvalue = num_cnt[i]
    elif num_cnt[i] == maxvalue:
        ans.append(int(i))
        maxvalue = num_cnt[i]
    else:
        continue

ans.sort()
print(ans[0])
