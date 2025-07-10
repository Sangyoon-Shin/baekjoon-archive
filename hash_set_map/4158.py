import sys
input = sys.stdin.readline

flag = 1
while True:
    try:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        a = {}
        b = {}
        for i in range(n):
            k = int(input())
            a[k] = 1
        for j in range(m):
            k = int(input())
            b[k] = 1
        
        cnt = 0
        for key in a.keys():
            if key in b:
                cnt += 1
        print(cnt)

    except Exception:
        break
