import sys
input = sys.stdin.readline

m, n, k, w = map(int, input().split())
matrix = [list(map(int, input().split())) for j in range(m)]
res = [[0 for i in range(n-w+1)] for i in range(m-w+1)]

tmp = []
for i in range(m - w + 1):
    for j in range(n - w + 1):
        for x in range(w):
            for y in range(w):
                tmp.append(matrix[i + x][j + y])
        tmp.sort()
        res[i][j] = tmp[len(tmp) // 2]
        tmp.clear()

for row in res:
    for val in row:
        print(val, end=' ')
    print()



