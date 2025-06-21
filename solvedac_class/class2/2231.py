n = int(input())

flag = 0

for i in range(1, n - 1):
    cur = i
    sumdigit = sum(map(int, str(cur)))
    m = cur + sumdigit
    if(m == n):
        print(cur)
        flag = 1
        break
    else:
        pass

if(flag == 0):
    print(0)
