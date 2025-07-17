import sys
input = sys.stdin.readline

while True:
    n = list(input().strip())
    if n[0] == '0':
        break
    else:
        sum = 0
        while True:
            n = list(map(int, n))
            for i in n:
                sum += i
            if sum < 10:
                print(sum)
                break
            else:
                sum = str(sum)
                n = sum
                sum = 0



