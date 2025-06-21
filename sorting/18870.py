# https://velog.io/@christer10/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A2%8C%ED%91%9C-%EC%95%95%EC%B6%95 참고

import sys
input = sys.stdin.readline

# 좌표 압축을 적용한 배열? => 나보다 작은 값이 몇 개 있는가에 대한 배열
n = int(input())
arr = list(map(int, input().split()))

ansarr = set(arr) # 중복은 제거. why? idx로 따질건데 같은 값이 여러개 있으면 idx 밀림.
ansarr = list(ansarr)
ansarr.sort()

# dict로 안만들면 이중 for문 돌려야해서 시간초과. (값, index)로 저장
ansarrdic = {}
for i in range(len(ansarr)):
    ansarrdic[ansarr[i]] = i

for i in arr:
    print(ansarrdic[i], end=' ')

