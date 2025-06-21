import sys

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(input().strip())

setarr = list(set(arr)) # 1. 리스트로 중복 제거
setarr.sort() # 2. 알파벳 순 정렬
setarr.sort(key = len) # 3. 단어 길이 순 정렬

# arr.sort: 배열 오름차순으로 변형. 반환 X
# sorted(arr): arr 배열 변형 X. 오름차순으로 정렬된 새로운 배열 반환

for i in range(len(setarr)):
    print(setarr[i])