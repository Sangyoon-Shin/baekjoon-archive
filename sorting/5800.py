import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    score = []
    for j in range(len(x) - 1):
        score.append(x[j + 1])
    score.sort()
    gap = []
    for j in range(len(score) - 1):
        gap.append(score[j + 1] - score[j])
    print(f"Class {i + 1}")
    print(f"Max {score[-1]}, Min {score[0]}, Largest gap {max(gap)}")
        
