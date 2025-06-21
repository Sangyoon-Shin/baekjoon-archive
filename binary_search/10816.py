import sys
input = sys.stdin.readline

# n = input()
# arr1 = list(map(int, input().split()))

# m = input()
# arr2 = list(map(int, input().split()))

# arr1.sort()

# for i in arr2:
#     start = 0
#     end = len(arr1) - 1
#     flag = 0
#     while(start <= end):
#         mid = (start + end) // 2
#         if(i == arr1[mid]):
#             cnt = arr1.count(i) # count 함수 시간복잡도 O(n). arr2에 대해서 다 해버리면 O(mn)
#             print(cnt, end=' ')
#             flag = 1
#             break
#         elif(i > arr1[mid]):
#             start = mid + 1
#         else:
#             end = mid - 1    
#     if(flag == 0):
#         print(0, end=' ')         
                

# 해시 사용
from collections import Counter
n = input()
arr1 = list(map(int, input().split()))
cntlist = Counter(arr1)

m = input()
arr2 = list(map(int, input().split()))

for idx in arr2:
    print(cntlist[idx], end=' ')