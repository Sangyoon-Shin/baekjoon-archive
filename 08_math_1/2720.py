import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    num = int(input())
    q, d, n, p = 0, 0, 0, 0
    while num > 0:
        if num >= 25:
            q = num // 25
            num %= 25
        elif num >= 10:
            d = num // 10
            num %= 10
        elif num >= 5:
            n = num // 5
            num %= 5
        elif num >= 1:
            p = num // 1
            num %= 1
    print(q, d, n, p)
            
