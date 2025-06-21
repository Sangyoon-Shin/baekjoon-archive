import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    prev = [i + 1 for i in range(14)]
    new = prev

    k = int(input())
    n = int(input())

    sum = 0
    if k == 1:
        for f in range(n):
            sum = sum + prev[f]
        print(sum)

    else:
        for x in range(1, k + 1): 
            sum = 0 
            for y in range(14):
                sum = sum + prev[y]
                new[y] = sum
        print(new[n - 1])


