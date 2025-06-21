import sys
input = sys.stdin.readline

# 파이썬에서 round는 .5 를 짝수가 되는 방향으로 반올림
# 2.5 => 2     3.5 => 4
def up(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
arr = []

for i in range(n):
    x = int(input())
    arr.append(x)

line = up(n * 0.15)

arr.sort()
arr = arr[line:n - line]

sumval = sum(arr)

# 아직 아무 의견이 없다면 문제의 난이도는 0.....
if len(arr) == 0:
    print(0)
else:
    print(up(sumval/len(arr)))

