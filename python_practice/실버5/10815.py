import sys
input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))
target.sort()

m = int(input())
cmp = list(map(int, input().split()))

for i in range(m):
    start = 0
    end = len(target) - 1
    flag = 0

    while start <= end:
        mid = (start + end) // 2
        if(cmp[i] > target[mid]):
            start = mid + 1
        elif(cmp[i] < target[mid]):
            end = mid - 1
        elif(cmp[i] == target[mid]):
            print('1', end=' ')
            flag = 1
            break
    if(flag == 0):
        print('0', end=' ')
    
                