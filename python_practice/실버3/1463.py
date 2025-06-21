def makeToZero(x):
    cnt = 0
    while True:
        if x == 1:
            print(cnt)
            return
        elif x % 3 == 0:
            x = x // 3
            cnt += 1
        elif x % 2 == 0:
            x = x // 2
            cnt += 1
        elif (x - 1) % 3 == 0:
            x -= 1
            cnt += 1
            x = x // 3
        elif (x - 1) % 2 == 0:
            x -= 1
            cnt += 1
            x = x // 2
        else:
            x -= 1
            cnt += 1

x = int(input())
makeToZero(x)
