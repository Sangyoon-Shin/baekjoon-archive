import sys
input = sys.stdin.readline

n = int(input())
total = list(map(int, input().split()))
total_score = sum(total)

myview = list(map(int, input().split()))
myview_score = 0
for i in range(len(myview)):
    if myview[i] == 0:
        myview_score += total[i]

print(total_score)
print(myview_score)
