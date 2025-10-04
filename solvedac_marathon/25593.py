import sys
input = sys.stdin.readline

n = int(input())
schedule = {}
flag = False

for i in range(4*n):
    if i % 4 == 0 or i % 4 == 2:
        t = 4
    elif i % 4 == 1:
        t = 6
    elif i % 4 == 3:
        t = 10
    
    name = list(input().rstrip().split())
    for na in name:
        if na == '-':
            pass
        elif na in schedule:
            schedule[na] += t
        else:
            schedule[na] = t
            flag = True

res = []

if flag == True:
    for key, val in schedule.items():
        res.append((key, val))
    res.sort(key=lambda x:x[1])
    diff = res[len(res) - 1][1] - res[0][1] 
    if diff > 12:
        print("No")
    else:
        print("Yes")
else:
    print("Yes")







    
    