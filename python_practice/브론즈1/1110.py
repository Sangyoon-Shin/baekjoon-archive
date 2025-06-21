n = int(input())

cnt = 0
firstnum = n

while(1):
    if n < 10:
        cnt += 1
        strn = '0' + str(n)
        sum = int(strn[0]) + int(strn[1])
        if sum > 9:
            overtensum = str(sum)
            if strn[1] == '0':
                newn = int(str(overtensum[1]))
            else:
                newn = int(strn[1] + str(overtensum[1]))
        else:
            if strn[1] == '0':
                newn = int(str(sum))
            else:
                newn = int(strn[1] + str(sum))

        n = newn
        if cnt > 0 and firstnum == newn:
            print(cnt)
            break
        else:
            continue

    else:
        cnt += 1
        strn = str(n)
        sum = int(strn[0]) + int(strn[1])
        if sum > 9:
            overtensum = str(sum)
            if strn[1] == '0':
                newn = int(str(overtensum[1]))
            else:
                newn = int(strn[1] + str(overtensum[1]))
        else:
            if strn[1] == '0':
                newn = int(str(sum))
            else:
                newn = int(strn[1] + str(sum))

        n = newn
        if cnt > 0 and firstnum == newn:
            print(cnt)
            break
        else:
            continue

