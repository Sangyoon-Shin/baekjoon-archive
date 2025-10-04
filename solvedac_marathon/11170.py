import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    # arr = []
    # for j in range(n, m + 1):
    #     arr.append(str(j))
    # cnt = 0
    # for k in range(len(arr)):
    #     for l in range(len(arr[k])):
    #         if arr[k][l] == '0':
    #             cnt += 1
    cnt = 0
    for j in range(n, m + 1):
        cnt += str(j).count("0")

    print(cnt)

