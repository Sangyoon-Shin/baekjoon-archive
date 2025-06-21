import sys
input = sys.stdin.readline

# 풀이 1.
# n1 = int(input())
# arr1 = list(map(int, input().split()))

# n2 = int(input())
# arr2 = list(map(int, input().split()))

# arr1.sort() # 정렬: O(nlogn)
  
# for i in arr2: # 이진탐색: O(nlogn)
#     start = 0
#     end = len(arr1) - 1
#     flag = 0
#     while(start <= end):
#         mid = (start + end) // 2
#         if(i == arr1[mid]):
#             print(1)
#             flag = 1
#             break
#         elif(i > arr1[mid]):
#             start = mid + 1
#         else:
#             end = mid - 1
#     if(flag == 0):
#         print(0)


# 풀이 2.
n1= int(input())
arr1 = set(list(map(int, input().split()))) # O(n)

n2 = int(input())
arr2 = list(map(int, input().split()))

for i in arr2: # O(n)
    print(1) if i in arr1 else print(0) # in: 보통 시간 복잡도 O(1), 최악 O(n). 거의 O(1)
