import sys
input = sys.stdin.readline

for i in range(3):
    str = input()
    flag = 0
    max = 0
    for j in range(7):
        cnt = 0
        if str[j] == str[j + 1]:
            k = j
            flag = 1
            while(str[k] == str[k + 1]):
                k += 1
                cnt += 1
        if cnt > max:
            max = cnt
    if flag == 0:
        print(1)
    else:
        print(cnt)
                