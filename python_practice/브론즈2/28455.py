import sys
input = sys.stdin.readline

n = int(input())

level = []
for i in range(n):
    l = int(input())
    level.append(l)

level.sort(reverse=True)

total, ability = 0, 0

if n < 42:
    for i in range(n):
        total += level[i]
        if level[i] >= 60 and level[i] < 100:
            ability += 1
        elif level[i] >= 100 and level[i] < 140:
            ability += 2
        elif level[i] >= 140 and level[i] < 200:
            ability += 3
        elif level[i] >= 200 and level[i] < 250:
            ability += 4
        elif level[i] >= 250:
            ability += 5

else:
    for i in range(42):
        total += level[i]
        if level[i] >= 60 and level[i] < 100:
            ability += 1
        elif level[i] >= 100 and level[i] < 140:
            ability += 2
        elif level[i] >= 140 and level[i] < 200:
            ability += 3
        elif level[i] >= 200 and level[i] < 250:
            ability += 4
        elif level[i] >= 250:
            ability += 5


print(total, end=' ')
print(ability)