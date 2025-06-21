# 1
# 1 + 6
# 1 + 6 + 12
# 1 + 6 + 12 + 18

n = int(input())

value = 6

cur = 1
prev = 0
cnt = 1
    
while(1):
    if(n <= cur and n >= prev):
        print(cnt)
        break
    else:
        prev = cur
        cur = cur + (value * cnt)
        cnt += 1
