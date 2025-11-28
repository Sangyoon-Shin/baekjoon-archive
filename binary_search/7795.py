import sys
input = sys.stdin.readline

def binary_search(value, arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[start] >= value:
            break
        if arr[mid] < value:
            start = mid + 1
        elif arr[mid] >= value:
            end = mid - 1
    res = start
    return res


t = int(input())
for i in range(t):
    n, m = map(int ,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    cnt = 0
    start = 0
    end = m - 1
    for j in range(n):
        cnt += binary_search(a[j], b, start, end)
    print(cnt)
    
