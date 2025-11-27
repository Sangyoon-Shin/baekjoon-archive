import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    maximum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                pass
            else:
                a = max(arr[i], arr[j])
                b = min(arr[i], arr[j])
                while True:
                    if a % b != 0:
                        tmp = a % b
                        a = b
                        b = tmp
                    else:
                        if b > maximum:
                            maximum = b
                        break
    print(maximum)
        

