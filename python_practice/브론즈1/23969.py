import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
found = False

for i in range(n - 1, 0, -1):
    swapped = False
    for j in range(i):
        if arr[j] > arr[j + 1]:
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j+ 1] = tmp
            cnt += 1
            swapped = True
            if cnt == k:
                print(*arr)
                found = True
                break
    if found:
        break
    if not swapped:
        break

if not found:
    print(-1)
