import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
newnum = {}
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
        else:
            newnum[i] -= 1
            s.append(i)
            dfs()
            s.pop()
            newnum[i] += 1

dfs()


    

