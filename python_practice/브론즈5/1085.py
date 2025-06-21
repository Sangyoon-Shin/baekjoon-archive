import sys

x, y, w, h = (0, 0, 0, 0)

x, y, w, h = map(int, input().split())
# x축(x, 0), y축(0, y), (x, h), (w, y) 중 가장 가까운 좌표가 답

shortest = 1001

arr = [x, y, w - x, h - y] 

# c언어에서는 arr[idx]가 idx에 해당하는 값이었음.
# 파이썬에서는 i 자체가 i번째 원소값
# for i in arr:
#     if(i < shortest):
#         shortest = i

# print(shortest)


# 다른 풀이
print(min(arr))
