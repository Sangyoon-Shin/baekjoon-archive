import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
newnum = {}
used = [False] * n

for i in num:
    if i not in newnum.keys():
        newnum[i] = 1
    else:
        newnum[i] += 1

nnewnum = list(newnum)
nnewnum.sort()
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in nnewnum:
        if newnum[i] == 0:
            continue
        if used[used.index(i)]:
            continue
        else:
            newnum[i] -= 1
            used[i] = True
            s.append(i)
            dfs()
            s.pop()
            newnum[i] += 1
            used[i] = False

dfs()


    

