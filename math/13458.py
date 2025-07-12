import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
main, sub = map(int, input().split())

total = 0
for i in a:
    k = i
    k -= main
    total += 1
    if k > 0:
        if k % sub == 0:
            total += k // sub
        else:
            total += k // sub + 1
    else:
        pass


print(total)
    


