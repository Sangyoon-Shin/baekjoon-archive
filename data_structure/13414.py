import sys
input = sys.stdin.readline

k, l = map(int, input().split())
idlist = {}
cntlist = {}
idinput = []
res = []

for i in range(l):
    stid = input().rstrip()
    idinput.append(stid)
    if stid in idlist:
        idlist[stid] += 1
    else:
        idlist[stid] = 1

# 입력받은 순서대로 cnt가 1번인 애들부터 넣고 두 번 이상 나온애들은 걔네들끼리 나온 횟수 세서 뒤에 넣어주기
for i in idinput:
    if i in cntlist:
        cntlist[i] += 1
        if cntlist[i] == idlist[i]:
            res.append(i)
    else:
        cntlist[i] = 1
        if cntlist[i] == idlist[i]:
            res.append(i)

for sid in res[:k]:
    print(sid)