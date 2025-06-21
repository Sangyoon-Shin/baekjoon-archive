import sys
input = sys.stdin.readline

score = {}
scorelist = []

for i in range(8):
    score[i + 1] = int(input())

for key, value in score.items():
    scorelist.append((key, value))

scorelist.sort(key=lambda x:-x[1])

sum = 0
idxlist = []
for i in range(5):
    sum = sum + scorelist[i][1]
    idxlist.append(scorelist[i][0])

print(sum)
idxlist.sort()
print(*idxlist)


