'''
A[0] = 2, A[1] = 3, A[2] = 1
P[0] = 1, P[1] = 2, P[2] = 0
수식에 적용시키면.. B[1] = 2, B[2] = 3, B[0] = 1
P수열은 A수열의 순서에 대한 정보임. 
'''

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
sorted_seq = sorted(seq)
res = []

for val in seq:
    res.append(sorted_seq.index(val))
    sorted_seq[sorted_seq.index(val)] = -1 # 이미 순회한 애는 -1로 해줘서 중복 피하기

print(*res)



