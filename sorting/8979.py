import sys
input = sys.stdin.readline

n, k = map(int, input().split())

record = []
for i in range(n):
    nat, gold, silver, bronze = map(int, input().split())
    record.append((nat, gold, silver, bronze))

record.sort(key=lambda x:(-x[1], -x[2], -x[3]))

rankdict = {}
medal = set()
rank = 1
for i in range(len(record)):
    # 등수 어떻게 뽑을지 생각해봐야 할 듯
    # 국가를 key, 등수를 value로. 메달 개수는 set에 넣어서 중복되었으면 이전 국가와 동일한 rank 부여, 아니면 rank++
    if record[i][0] in rankdict.keys():
        pass
    else:
        if (record[i][1], record[i][2], record[i][3]) in medal:
            rankdict[record[i][0]] = rankdict[record[i - 1][0]]
            rank += 1
        else:
            rankdict[record[i][0]] = rank
            medal.add((record[i][1], record[i][2], record[i][3]))
            rank += 1

print(rankdict[k])


