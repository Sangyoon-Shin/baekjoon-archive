import sys
input = sys.stdin.readline

res = [True for i in range(1001)]

for i in range(1, 1001):
    i = str(i)
    stringlist = list(i)
    flag = 0
    if len(stringlist) >= 3:
        for j in range(len(stringlist) - 1):
            if j == 0:
                gap = int(stringlist[j + 1]) - int(stringlist[j])
            else:
                curgap = int(stringlist[j + 1]) - int(stringlist[j])
                if curgap != gap:
                    flag = 1
                    value = int(''.join(stringlist))
                    res[value] = False
    else:
        pass

n = int(input())

cnt = 0
for i in range(1, n + 1):
    if res[i] == True:
        cnt += 1

print(cnt)
