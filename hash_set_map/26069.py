import sys
input = sys.stdin.readline

n = int(input())

dance = {}
start = 0

for i in range(n):
    prev, cur = map(str, input().strip().split())
    if start == 0 and prev != 'ChongChong' and cur != 'ChongChong':
        pass
    elif (cur == 'ChongChong' and start == 0) or (prev == 'ChingChong' and start == 0):
        start = 1
        dance[cur] = 1
        dance[prev] = 1
    # 1. prev는 춤추는중, cur는 춤 안추는중 + 총총이가 춤을 춘상태
    elif prev in dance.keys() and cur not in dance.keys() and start == 1:
        dance[cur] = 1
    # 2. prev는 춤 X. cur는 춤 O + 총총이 O
    elif prev not in dance.keys() and cur in dance.keys() and start == 1:
        dance[prev] = 1
    # 3. prev, cur 둘 다 춘 상태면 pass
    elif prev in dance.keys() and cur in dance.keys() and start == 1:
        pass
    # 4. 둘 다 춤 안 춘 상태면 pass
    elif prev not in dance.keys() and cur not in dance.keys() and start == 1:
        pass

cnt = 0
for key in dance.keys():
    if dance[key] >= 1:
        cnt += 1

print(cnt)
        

