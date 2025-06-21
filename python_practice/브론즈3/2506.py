import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

totalsum = 0
cnt = 0

for i in range(1, len(score)):
    if score[i] == 1:
        if score[i - 1] == 1:
            cnt += 1
            totalsum = totalsum + cnt*1
        elif score[i - 1] == 0:
            totalsum += 1
            cnt += 1
    
    else:
        pass

print(totalsum)
        




        
