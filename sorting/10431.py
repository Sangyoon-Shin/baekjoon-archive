import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    test_num = data[0]
    arr = data[1:]
    cnt = 0

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                cnt += 1
    print(test_num, cnt)
