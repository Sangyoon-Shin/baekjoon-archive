import sys
input = sys.stdin.readline

n = int(input())
score = []

for i in range(n):
    score.append(int(input()))

if score[0] == max(score):
    print("hard")
else:
    if score[0] == min(score):
        print("ez")
    else:
        print("?")