import sys

n = int(input())

arr = []


arr = list(map(int, sys.stdin.readline().split()))

# 12의 약수: [1, 2, 3, 4, 6, 12] -> 1은 입력 X. A != N이므로 12도 못들어옴. 2 * 6 = 12
value = min(arr) * max(arr)
print(value)
