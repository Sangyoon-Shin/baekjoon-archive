import sys
input = sys.stdin.readline

score = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}

scores = list(input())

cnt = 0
total = 0
for i in range(len(scores) - 1):
    if scores[i] == '+':
        pass
    else:
        if scores[i + 1] == '+':
            rank = scores[i] + scores[i + 1]
            total += score[rank]
            cnt += 1
        else:   
            total += score[scores[i]]
            cnt += 1

print(f"{total/cnt:.4f}")
